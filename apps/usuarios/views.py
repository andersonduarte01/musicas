from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from ..usuarios.models import UsuarioCad
from ..usuarios.forms import UserCreationUsuario


# Create your views here.


class CadastrarUser(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = UsuarioCad
    form_class = UserCreationUsuario
    template_name = 'usuarios/adicionar_usuario.html'
    success_message = 'Cadastro Realizado com sucesso!'
    success_url = reverse_lazy('login')
