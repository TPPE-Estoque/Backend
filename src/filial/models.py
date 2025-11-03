from django.db import models

class Filial(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    cep = models.CharField(max_length=9)
    logradouro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)

    gerente_id = models.IntegerField(null=True, blank=True, unique=True)

    esta_ativa = models.BooleanField(default=True, help_text="Indica se a filial está ativa")

    def __str__(self):
        return self.nome
