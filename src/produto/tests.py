import unittest
from django.test import TestCase
from rest_framework.test import APITestCase

class TestesAPIProduto(APITestCase):
    """
    Suite de testes para a API de Produtos.
    """
    @unittest.skip("TODO: Implementar teste de listagem de produtos via API.")
    def test_lista_produtos_endpoint(self):
        pass

class TestesModelProduto(TestCase):
    """
    Suite de testes para o Model de Produto.
    """
    @unittest.skip("TODO: Implementar teste de criação do modelo Produto.")
    def test_criacao_de_produto(self):
        pass
