from django.urls import path
from . import views

app_name = 'album'

urlpatterns = [
    path('<int:album>/musicas/', views.MusicaView.as_view(), name='arquivos_musicais'),
    path('genero/', views.AddEstilo.as_view(), name='add_estilo'),
    path('lista/generos/', views.ListaEstilos.as_view(), name='lista_estilos'),
    path('adicionar/', views.AddAlbum.as_view(), name='add_album'),
    path('lista/', views.ListaAlbuns.as_view(), name='lista_albuns'),
    path('songs/<int:album>/', views.MusicasLista.as_view(), name='musicas'),
    ####
    path('genero/<str:nacionalidade>/', views.Nacionalidade.as_view(), name='nacionalidade'),
    path('<str:estilo>/genero/', views.Genero.as_view(), name='genero'),
    ## REST API ##

    path('api/v1/estilos/', views.EstiloApiView.as_view(), name='estilos_serial'),
    path('api/v1/albuns/', views.AlbumApiView.as_view(), name='albuns_serial'),
    path('musicas_seriais/', views.MusicaApiView.as_view(), name='musicas_serial'),
]
