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

    path('api/v1/estilos/', views.EstilosApiView.as_view(), name='estilos_serial'),
    path('api/v1/estilo/<int:pk>/', views.EstiloApiView.as_view(), name='estilo_serial'),
    path('api/v1/albuns/', views.AlbunsApiView.as_view(), name='albuns_serial'),
    path('api/v1/selecao/estilo/albuns/<int:pk>/', views.AlbunsEstiloApiView.as_view(), name='albuns_estilo_serial'),
    path('api/v1/album/<int:pk>/', views.AlbumApiView.as_view(), name='album_serial'),
    path('api/v1/musicas/', views.MusicasApiView.as_view(), name='musicas_serial'),
    path('api/v1/musica/<int:pk>/', views.MusicaApiView.as_view(), name='musica_serial'),
    #path('api/v1/musicas/6', views.LewisApiView.as_view(), name='lewis_serial'),
]
