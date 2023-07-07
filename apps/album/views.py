from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView
from .forms import MusicaForm
from .models import Estilo, Album, Musica
from ..core.models import Usuario
import unicodedata


class AddEstilo(CreateView):
    model = Estilo
    fields = ('estilo', 'nacionalidade')
    template_name = 'album/estilo_add.html'
    success_url = '/'


class ListaEstilos(ListView):
    model = Estilo
    template_name = 'album/lista_estilos.html'
    context_object_name = 'estilos'


class AddAlbum(LoginRequiredMixin, CreateView):
    model = Album
    fields = ('nome_album', 'capa', 'estilo', 'cantor')
    template_name = 'album/album_add.html'

    def form_valid(self, form):
        album = form.save(commit=False)
        usuario = Usuario.objects.get(pk=self.request.user.id)
        album.usuario = usuario
        album.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('album:arquivos_musicais', kwargs={'album': self.object.id})


class ListaAlbuns(ListView):
    model = Album
    template_name = 'album/lista_albuns.html'
    context_object_name = 'albuns'
    ordering = ('-atualizado',)


class MusicaView(FormView):
    form_class = MusicaForm
    template_name = "album/add_musica.html"  # Replace with your template.

    def get_success_url(self):
        return reverse('album:musicas', kwargs={'album': self.kwargs['album']})

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        files = form.cleaned_data["arquivo_musical"]
        album = Album.objects.get(id=self.kwargs['album'])

        for file in files:
            m = f'{file}'
            m2 = f'{file}'
            titulo_musica = m.replace(".mp3", "")

            processamento_2 = unicodedata.normalize("NFD", m2)
            processamento_2 = processamento_2.encode("ascii", "ignore")
            processamento_2 = processamento_2.decode("utf-8")

            file.name = processamento_2
            musica = Musica.objects.create(musica=titulo_musica, arquivo_musical=file, album=album)
        return super().form_valid(form)


class MusicasLista(ListView):
    model = Musica
    template_name = 'album/musicas.html'
    context_object_name = 'musicas'

    def get_queryset(self):
        album = Album.objects.get(pk=self.kwargs['album'])
        return Musica.objects.filter(album=album)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        album = Album.objects.get(pk=self.kwargs['album'])
        context['album'] = album
        return context


class Nacionalidade(ListView):
    model = Album
    template_name = 'album/generos.html'
    context_object_name = 'albuns'


    def get_queryset(self):
        generos = Estilo.objects.filter(nacionalidade=self.kwargs['nacionalidade'])
        return Album.objects.filter(estilo__in=generos).order_by('-atualizado')


class Genero(ListView):
    model = Album
    template_name = 'album/generos_especificos.html'
    context_object_name = 'albuns'


    def get_queryset(self):
        generos = Estilo.objects.filter(estilo=self.kwargs['estilo'])
        return Album.objects.filter(estilo__in=generos).order_by('-atualizado')




