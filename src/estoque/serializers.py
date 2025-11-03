from rest_framework import serializers

from produto.models import Produto
from produto.serializers import ProdutoSerializer

from .models import ItemEstoque


class ItemEstoqueSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer(read_only=True)

    produto_id = serializers.PrimaryKeyRelatedField(
        queryset=Produto.objects.all(), source="produto", write_only=True
    )

    class Meta:
        model = ItemEstoque
        fields = [
            "id",
            "produto",
            "produto_id",
            "quantidade_atual",
            "preco_venda_atual",
            "quantidade_minima_estoque",
        ]
