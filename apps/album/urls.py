from django.urls import path
from . import views

app_name = 'album'

urlpatterns = [
    path('<int:album>/musicas/', views.MusicaView.as_view(), name='arquivos_musicais'),
    path('estilo/', views.AddEstilo.as_view(), name='add_estilo'),
    path('lista/estilos/', views.ListaEstilos.as_view(), name='lista_estilos'),
    path('adicionar/', views.AddAlbum.as_view(), name='add_album'),
    path('lista/', views.ListaAlbuns.as_view(), name='lista_albuns'),
    path('<int:album>/songs/', views.MusicasLista.as_view(), name='musicas'),
]
