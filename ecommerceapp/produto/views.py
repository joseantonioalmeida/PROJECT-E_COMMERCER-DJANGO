from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse


# Create your views here.
class ListaProdutos(ListView):
    def get(self, *args, **kwargs):
        return HttpResponse('Lista Produto')
class DetalheProduto(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhe do produto')
class AdicionarAoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Adicionar')
class RemoverDoCarinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Remover')
class Carrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Caarrinho')
class Finalizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finalizar')