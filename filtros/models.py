from django.db import models

class Produtos(models.Model):
    nome = models.CharField(max_length=90)
    descricao = models.TextField(blank=True, null=True)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    id_categoria = models.IntegerField(blank=True, null=True)
    no_categoria = models.CharField(blank=True, null=True)
    no_loja = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'produtos'
class ListaProduto(models.Model):
    nome = models.CharField()
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    is_ativo = models.BooleanField(blank=True, null=True)
    quantidade = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lista_produto'
