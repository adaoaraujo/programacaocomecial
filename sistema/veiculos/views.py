from django.views.generic import View
from django.shortcuts import render
from veiculos.models import Veiculo

# Create your views here.

class VeiculosList(View):

    def get(self,request):
        contexto = {
            'lista_veiculos' :Veiculo.objects.all().order_by('marca')
        } 
        return render(request,'veiculos/listar.html',contexto)
