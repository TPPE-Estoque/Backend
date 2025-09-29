from rest_framework import serializers
from .models import Produto

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'codigo_barras', 'nome', 'descricao', 'tipo', 'ativo']