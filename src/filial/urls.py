from django.urls import path
from .views import FilialListCreateView, FilialDetailView

urlpatterns = [
    path('', FilialListCreateView.as_view(), name='filial-lista-criar'),
    path('<int:pk>/', FilialDetailView.as_view(), name='filial-detalhe'),
]
