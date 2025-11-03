from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import FormaPagamento, Venda
from .serializers import (
    AdicionarItemVendaSerializer,
    ItemVendaSerializer,
    VendaSerializer,
)


class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Venda.objects.filter(usuario_id=self.request.user.id)

    def perform_create(self, serializer):
        usuario_id = self.request.user.id
        serializer.save(usuario_id=usuario_id)

    @action(detail=True, methods=["post"], serializer_class=AdicionarItemVendaSerializer)
    def adicionar_item(self, request, pk=None):
        venda = self.get_object()
        if venda.status != Venda.StatusVenda.ABERTA:
            return Response(
                {"detail": "Não é possível adicionar itens a uma venda finalizada."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = AdicionarItemVendaSerializer(data=request.data, context={"venda": venda})
        if serializer.is_valid():
            item = serializer.save()

            return Response(ItemVendaSerializer(item).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["post"])
    def finalizar_venda(self, request, pk=None):
        venda = self.get_object()
        forma_pagamento_str = request.data.get("forma_pagamento")

        try:
            forma_pagamento_enum = FormaPagamento(forma_pagamento_str)
        except ValueError:
            return Response(
                {"detail": "Forma de pagamento inválida."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            venda.finalizar_venda(forma=forma_pagamento_enum)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(VendaSerializer(venda).data, status=status.HTTP_200_OK)
