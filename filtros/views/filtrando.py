from django.shortcuts import render

from filtros.models import Produtos, ListaProduto

def lista_tabelas(request):
    produto = Produtos.objects.all()
    lista_produto = ListaProduto.objects.all()
    
    context = {
        
    }
    return render(request, 'index.html', context = context)