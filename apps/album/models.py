from django.db import models
from stdimage import StdImageField
from ..core.models import Usuario

# Create your models here.


class Estilo(models.Model):

    NACIONALIDADE = [
        ('NACIONAL', 'Nacional'),
        ('INTERNACIONAL', 'Internacional'),

    ]

    estilo = models.CharField(verbose_name='Gênero', max_length=155)
    nacionalidade = models.CharField(verbose_name='Nacionalidade', max_length=50, choices=NACIONALIDADE)

    def __str__(self):
        return self.estilo

    class Meta:
        verbose_name = 'Gênero'
        verbose_name_plural = 'Gêneros'


class Album(models.Model):
    nome_album = models.CharField(verbose_name='Álbum', max_length=200)
    capa = StdImageField(upload_to='capa/album', variations={'thumbnail': {'width': 400, 'height': 400}},
                         null=True, blank=True, delete_orphans=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    estilo = models.ForeignKey(Estilo, on_delete=models.DO_NOTHING)
    cantor = models.CharField(verbose_name='Cantor', max_length=255)
    status = models.BooleanField(verbose_name='Status', default=True)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome_album

    def imagem(self):
        if self.capa:
            return True
        else:
            return False

    class Meta:
        verbose_name = 'Álbum'
        verbose_name_plural = 'Álbuns'


class Musica(models.Model):
    musica = models.CharField(verbose_name='Música', max_length=200)
    arquivo_musical = models.FileField(upload_to='arquivos/musicas', verbose_name='Upload Arquivo')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='musica_album')
    status = models.BooleanField(verbose_name='Status', default=True)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.musica

    class Meta:
        verbose_name = 'Música'
        verbose_name_plural = 'Músicas'

