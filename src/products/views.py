from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.generics import ListAPIView
from .models import Produto
from .serializers import ProductSerializer

class HelloWorldView(APIView):
    def get(self, request, *args, **kwargs):
        data = {"message": "Hello World!"}
        return Response(data, status=status.HTTP_200_OK)

class ProductListView(ListAPIView):
    queryset = Produto.objects.filter(ativo=True)
    serializer_class = ProductSerializer
