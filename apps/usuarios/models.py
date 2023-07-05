from django.db import models
from ..core.models import Usuario
# Create your models here.


class UsuarioCad(Usuario):
    SEXO = [
        ('MASCULINO', 'Masculino'),
        ('FEMININO', 'Feminino'),

    ]
    data_nascimento = models.CharField(verbose_name='Data de Nascimento', help_text='dd/mm/aaaa', max_length=20)
    sexo = models.CharField(verbose_name='Sexo', choices=SEXO, max_length=40)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
