from rest_framework.generics import ListAPIView
from .models import Produto
from .serializers import ProdutoSerializer

class ProdutoListView(ListAPIView):
    queryset = Produto.objects.filter(esta_ativo=True)
    serializer_class = ProdutoSerializer
