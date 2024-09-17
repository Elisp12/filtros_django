from django.shortcuts import render

from filtros.models import Produtos, ListaProduto

def lista_tabelas(request):
    produto = Produtos.objects.all()
    lista_produto = ListaProduto.objects.all()
    
    for p in produto:
        new_nome = p.nome
        new_descricao = p.descricao
        new_preco = p.preco
        new_quantidade = p.quantidade
        
        lista_produto.filter(nome = p.nome).update(
            nome = new_nome,
            descricao = new_descricao,
            preco = new_preco,
            quantidade = new_quantidade
        )    
        
    context = {
        
    }
    return render(request, 'index.html', context = context)