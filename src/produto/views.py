from rest_framework import generics, permissions

from .models import Produto
from .serializers import ProdutoSerializer


class ProdutoListCreateView(generics.ListCreateAPIView):
    serializer_class = ProdutoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Produto.objects.filter(esta_ativo=True)


class ProdutoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        instance.esta_ativo = False
        instance.save()
