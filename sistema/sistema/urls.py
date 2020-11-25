from django.contrib import admin
from django.urls import path, include
from sistema.views import Autenticacao

urlpatterns = [
    path("", Autenticacao.as_view(), name='index'),
    path('veiculos/', include('veiculos.urls')),
    path('admin/', admin.site.urls),
]


