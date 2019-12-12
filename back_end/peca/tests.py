from django.test import TestCase
import unittest
from .models import Peca

# Create your tests here.

class PecaTest(unittest.TestCase):

    def testEstoque(self):
        self.teste = Peca.objects.create(nome="Carburador",preco=449.90,estoque=2)
        self.assertFalse(self.teste.disponivel(0))

    def testNome(self):
        self.teste = Peca.objects.create(nome="Embreagem",preco=449.90,estoque=2)
        self.assertEquals(self.teste.getNome(),"Roda")