from rest_framework import generics, serializers

from estoque.models import ItemEstoque
from produto.models import Produto

from .models import FormaPagamento, ItemVenda, Venda


class ItemVendaSerializer(serializers.ModelSerializer):
    produto_nome = serializers.CharField(source="produto.nome", read_only=True)

    produto_id = serializers.PrimaryKeyRelatedField(
        queryset=Produto.objects.all(), source="produto", write_only=True
    )

    class Meta:
        model = ItemVenda
        fields = [
            "id",
            "produto_id",
            "produto_nome",
            "quantidade_vendida",
            "preco_vendido",
        ]
        read_only_fields = ["preco_vendido"]


class VendaSerializer(serializers.ModelSerializer):
    itens_venda = ItemVendaSerializer(many=True, read_only=True)

    forma_pagamento_finalizar = serializers.ChoiceField(
        choices=FormaPagamento.choices, write_only=True, required=False
    )

    class Meta:
        model = Venda
        fields = [
            "id",
            "filial",
            "usuario_id",
            "data_venda",
            "status",
            "forma_pagamento",
            "valor_total",
            "itens_venda",
            "forma_pagamento_finalizar",
        ]
        read_only_fields = [
            "valor_total",
            "forma_pagamento",
            "status",
            "data_venda",
            "usuario_id",
        ]

    # def create(self, validated_data):
    #     usuario_id = self.context['request'].user.id
    #     venda = Venda.objects.create(usuario_id=usuario_id, **validated_data)
    #     return venda


class AdicionarItemVendaSerializer(serializers.Serializer):
    produto_id = serializers.IntegerField()
    quantidade = serializers.FloatField()

    def validate_quantidade(self, value):
        if value <= 0:
            raise serializers.ValidationError("Quantidade deve ser positiva.")
        return value

    def create(self, validated_data):
        venda = self.context["venda"]
        produto = generics.get_object_or_404(Produto, id=validated_data["produto_id"])
        quantidade = validated_data["quantidade"]

        try:
            item_estoque = ItemEstoque.objects.get(filial=venda.filial, produto=produto)
            preco_atual = item_estoque.preco_venda_atual

            if item_estoque.quantidade_atual < quantidade:
                raise serializers.ValidationError(
                    f"Estoque insuficiente. Disponível: {item_estoque.quantidade_atual}"
                )

        except ItemEstoque.DoesNotExist:
            raise serializers.ValidationError("Produto não está no estoque desta filial.")

        item = ItemVenda.objects.create(
            venda=venda,
            produto=produto,
            quantidade_vendida=quantidade,
            preco_vendido=preco_atual,
        )
        venda.calcular_valor_total()
        return item
