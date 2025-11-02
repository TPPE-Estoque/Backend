from rest_framework import serializers
from .models import Filial

class FilialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filial
        fields = ['id', 'nome', 'cep', 'logradouro', 'cidade', 'estado', 'gerente_id', 'esta_ativa']
        read_only_fields = ['esta_ativa']
