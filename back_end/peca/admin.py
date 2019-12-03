from django.contrib import admin

# Register your models here.
from .models import Peca, Desconto, DescontoPeca, Carrinho

admin.site.register(Peca)
admin.site.register(Desconto)
admin.site.register(DescontoPeca)
admin.site.register(Carrinho)