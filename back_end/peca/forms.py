from django import forms
from .models import Peca, Desconto

class PecaForm(forms.ModelForm):
    class Meta:
        model = Peca
        fields = [
            'nome',
            'preco',
            'estoque'
        ]

class DescontoForm(forms.ModelForm):
    class Meta:
        model = Desconto
        fields = ['valor']