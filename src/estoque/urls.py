from django.urls import path
from .views import ItemEstoqueListCreateView, ItemEstoqueDetailView

app_name = 'estoque'

urlpatterns = [
    path('', ItemEstoqueListCreateView.as_view(), name='estoque-lista-criar'),
    path('<int:pk>/', ItemEstoqueDetailView.as_view(), name='estoque-detalhe'),
]
