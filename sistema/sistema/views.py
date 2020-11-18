 
from django.views.generic import View
from django.shortcuts import render


class Autenticacao(View):

    def get(self,request):
        contexto = {
            'usuario': '',
            'senha':''
        }
        return render(request,'autenticacao.html',contexto)  
   