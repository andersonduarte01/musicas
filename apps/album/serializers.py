from rest_framework import serializers

from .models import Estilo, Album, Musica

class EstiloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estilo
        fields = (
            'id',
            'estilo',
            'nacionalidade'
        )

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = (
            'id',
            'nome_album',
            'capa',
            'usuario',
            'estilo',
            'cantor',
            'status',
            'criado',
            'atualizado'
        )


class MusicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musica
        fields = (
            'id',
            'musica',
            'arquivo_musical',
            'album',
            'status',
            'criado',
            'atualizado'
        )
