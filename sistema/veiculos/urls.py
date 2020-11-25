from django.urls import path
from veiculos import views

urlpatterns = [
    path('',views.VeiculosList.as_view(), name='listar-veiculos'),
]

'''
from django.views.generic import ListView, createView
#from django.urls import reverse_lazy
from veiculos.models import Veiculo
#from veiculos.forms import FormularioVeiculo

class veiculosList(ListView):

    model = Veiculo
    context_object_name = 'lista_veiculos'
    template_name = 'veiculos/listar.html'
'''