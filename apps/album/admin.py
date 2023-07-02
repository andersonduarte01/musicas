from django.contrib import admin
from .models import Album, Estilo, Musica
# Register your models here.


class EstiloAdmin(admin.ModelAdmin):
    list_display = ('estilo', 'nacionalidade')


admin.site.register(Estilo, EstiloAdmin)


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('nome_album', 'usuario', 'cantor', 'estilo')


admin.site.register(Album, AlbumAdmin)


class MusicaAdmin(admin.ModelAdmin):
    list_display = ('musica', 'album')


admin.site.register(Musica, MusicaAdmin)
