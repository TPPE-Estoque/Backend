from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from produto.models import Produto
from filial.models import Filial
from .models import ItemEstoque
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class TestesAPIItemEstoque(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='userteste_estoque', password='testpassword123')
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        self.filial = Filial.objects.create(
            nome="Filial de Teste Estoque",
            cep="70000-000",
            cidade="Brasilia",
            estado="DF",
        )
        self.produto = Produto.objects.create(
            codigo_barras="1234567890000",
            nome="Produto para Estoque",
            tipo_produto='UNITARIO'
        )

    def test_adicionar_item_estoque_sucesso(self):
        url = reverse('estoque:estoque-lista-criar', kwargs={'filial_pk': self.filial.pk})
        data = {
            "produto_id": self.produto.pk,
            "quantidade_atual": 100.0,
            "preco_venda_atual": 25.50,
            "quantidade_minima_estoque": 10.0
        }
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ItemEstoque.objects.count(), 1)
        self.assertEqual(response.data['quantidade_atual'], 100.0)

    def test_adicionar_item_duplicado_falha(self):
        ItemEstoque.objects.create(
            filial=self.filial,
            produto=self.produto,
            preco_venda_atual=25.50
        )
        
        url = reverse('estoque:estoque-lista-criar', kwargs={'filial_pk': self.filial.pk})
        data = {
            "produto_id": self.produto.pk,
            "quantidade_atual": 50.0,
            "preco_venda_atual": 30.00,
            "quantidade_minima_estoque": 5.0
        }
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_listar_estoque_filial_sucesso(self):
        ItemEstoque.objects.create(
            filial=self.filial,
            produto=self.produto,
            preco_venda_atual=25.50,
            quantidade_atual=150
        )
        
        url = reverse('estoque:estoque-lista-criar', kwargs={'filial_pk': self.filial.pk})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['produto']['nome'], "Produto para Estoque")
