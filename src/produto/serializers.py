from rest_framework import serializers

from .models import Produto


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = [
            "id",
            "codigo_barras",
            "nome",
            "descricao",
            "tipo_produto",
            "esta_ativo",
        ]
