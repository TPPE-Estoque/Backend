from django.db import models

class Produto(models.Model):
    CODIGO_BARRAS_MAX_LENGTH = 13
    NOME_MAX_LENGTH = 100

    codigo_barras = models.CharField(max_length=CODIGO_BARRAS_MAX_LENGTH, unique=True, help_text="Código de barras")
    nome = models.CharField(max_length=NOME_MAX_LENGTH)
    descricao = models.TextField(blank=True, null=True)

    TIPO_PRODUTO_CHOICES = [
        ('UNITARIO', 'Produto Unitário'),
        ('PESAVEL', 'Produto Pesável'),
    ]
    tipo = models.CharField(max_length=10, choices=TIPO_PRODUTO_CHOICES, default='UNITARIO')

    ativo = models.BooleanField(default=True, help_text="Indica se o produto está ativo no catálogo")

    def __str__(self):
        return f"{self.nome} ({self.codigo_barras})"
