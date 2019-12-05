from django.db import models
from django.conf import settings

# Create your models here.
class Peca(models.Model):
    nome = models.CharField(max_length=75)
    preco = models.DecimalField(max_digits=6,decimal_places=2)
    estoque = models.PositiveIntegerField()

class Desconto(models.Model):
    valor = models.DecimalField(max_digits=4,decimal_places=2)

class DescontoPeca(models.Model):
    peca = models.ForeignKey('Peca', on_delete=models.CASCADE)
    desconto = models.ForeignKey('Desconto', on_delete=models.CASCADE)

class PecaCarrinho(models.Model):
    peca = models.ForeignKey('Peca',on_delete=models.CASCADE)
    qtde = models.PositiveIntegerField()
    

class Carrinho(models.Model):
    pecas = models.ManyToManyField('PecaCarrinho')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    realizado = models.BooleanField(default=False)
    total = models.DecimalField(max_digits=10,decimal_places=2)