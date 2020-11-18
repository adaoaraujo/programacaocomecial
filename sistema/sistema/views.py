from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

class Autenticacao(View):

    def get(self,request):
        contexto= {
            'usuario': '',
            'senha':''
        }
        return  render(request,'autenticacao.html',contexto)

    def post(self, request):

        usuario = request.POST.get('usuario',None)
        senha = request.POST.get('senha', None)

        logger.info('Usuario : {usuario}'.format(usuario=usuario))
        logger.info('Senha : {senha}'.format(senha=senha))
        
         # return HttpResponse('Em desenvolvimento')

        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('Usuario autenticado com sucesso')

            return render(request, 'autenticacao.html', {'mensagem': 'Usuario inativo'})

        return render(request, 'autenticacao.html', {'mensagem ': 'Usuario ou senha incorretos'})