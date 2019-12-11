from django.contrib import admin

# Register your models here.
from .models import Peca, Desconto, DescontoPeca, Carrinho,PecaCarrinho

admin.site.register(Peca)
admin.site.register(Desconto)
admin.site.register(DescontoPeca)
admin.site.register(Carrinho)
admin.site.register(PecaCarrinho)