from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import ItemEstoque, Filial
from .serializers import ItemEstoqueSerializer

class ItemEstoqueListCreateView(generics.ListCreateAPIView):
    serializer_class = ItemEstoqueSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_filial(self):
        filial_pk = self.kwargs.get('filial_pk')
        return generics.get_object_or_404(Filial, pk=filial_pk)

    def get_queryset(self):
        return ItemEstoque.objects.filter(filial=self.get_filial())

    def perform_create(self, serializer):
        filial = self.get_filial()

        produto = serializer.validated_data.get('produto')
        if ItemEstoque.objects.filter(filial=filial, produto=produto).exists():
            raise serializers.ValidationError("Este produto já existe no estoque desta filial.")

        serializer.save(filial=filial)

class ItemEstoqueDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemEstoqueSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        filial_pk = self.kwargs.get('filial_pk')
        return ItemEstoque.objects.filter(filial_id=filial_pk)

    def get_object(self):
        queryset = self.get_queryset()
        item_pk = self.kwargs.get('pk')
        return generics.get_object_or_404(queryset, pk=item_pk)

    def perform_destroy(self, instance):
        instance.delete()
