from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    comum = models.BooleanField()

class ClienteFixo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    empresa = models.CharField(max_length = 50)
    cnpj = models.CharField(max_length = 14)
    cep = models.CharField(max_length = 9)
    endereco = models.CharField(max_length = 100)
    telefone = models.CharField(max_length = 14)