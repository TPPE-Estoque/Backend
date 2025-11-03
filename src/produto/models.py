from django.db import models


class Produto(models.Model):
    CODIGO_BARRAS_MAX_LENGTH = 13
    NOME_MAX_LENGTH = 100

    class TipoProdutoChoices(models.TextChoices):
        UNITARIO = "UNITARIO", "Produto Unitário"
        PESAVEL = "PESAVEL", "Produto Pesável"

    codigo_barras = models.CharField(
        max_length=CODIGO_BARRAS_MAX_LENGTH,
        unique=True,
        help_text="Código de barras universal (EAN)",
    )
    nome = models.CharField(max_length=NOME_MAX_LENGTH)
    descricao = models.TextField(blank=True, null=True)

    tipo_produto = models.CharField(
        max_length=10,
        choices=TipoProdutoChoices.choices,
        default=TipoProdutoChoices.UNITARIO,
    )

    esta_ativo = models.BooleanField(
        default=True, help_text="Indica se o produto está ativo no catálogo"
    )

    def __str__(self):
        return f"{self.nome} ({self.codigo_barras})"
