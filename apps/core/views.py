from django.shortcuts import render
from django.views.generic import ListView
from ..album.models import Album


# Create your views here.


class Index(ListView):
    model = Album
    template_name = 'core/home.html'
    context_object_name = 'albuns'

    def get_queryset(self):
        return Album.objects.filter().order_by('-atualizado')[:6]



