from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/produtos/', include('produto.urls')),

    path('api/filiais/', include('filial.urls')),
]
