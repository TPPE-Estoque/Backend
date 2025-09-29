import unittest
from django.test import TestCase
from rest_framework.test import APITestCase

class ProductAPITestCase(APITestCase):
    @unittest.skip("TODO: Implementar teste de listagem de produtos via API.")
    def test_lista_produtos_endpoint(self):
        """
        Teste para verificar se o endpoint de listagem de produtos (GET /api/products/)
        está funcionando corretamente.
        """
        pass

    @unittest.skip("TODO: Implementar teste de criação de produto via API.")
    def test_cria_produto_endpoint(self):
        """
        Teste para verificar a criação de um novo produto através do endpoint
        (POST /api/products/).
        """
        pass


class ProductModelTestCase(TestCase):
    """
    Suite de testes para o Model de Produto.
    Herda de TestCase do Django para testes de unidade do modelo.
    """

    @unittest.skip("TODO: Implementar teste de criação do modelo Produto.")
    def test_criacao_de_produto(self):
        """
        Teste para verificar se um objeto do modelo Produto pode ser criado
        com os atributos corretos.
        """
        pass
