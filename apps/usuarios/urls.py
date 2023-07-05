from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('cadastrar/', views.CadastrarUser.as_view(), name='adicionar'),
]
