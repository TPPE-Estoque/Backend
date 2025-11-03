from django.urls import path

from .views import ProdutoDetailView, ProdutoListCreateView

app_name = "produto"

urlpatterns = [
    path("", ProdutoListCreateView.as_view(), name="produto-lista-criar"),
    path("<int:pk>/", ProdutoDetailView.as_view(), name="produto-detalhe"),
]
