from django.db import models

# Create your models here.
class Peca(models.Model):
    nome = models.CharField(max_length=75)
    codigo = models.PositiveSmallIntegerField()
    preco = models.DecimalField(max_digits=6,decimal_places=2)