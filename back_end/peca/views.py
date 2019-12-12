from django.shortcuts import render, redirect
from .models import *
from .forms import PecaForm, DescontoForm
from datetime import datetime

# Create your views here.

def index_view(request):
    return render(request, "index.html")

def login_view(request):
    return render(request, "_paginas/logar.html")

def verifica_view(request):
    return render(request, "_paginas/verificadorCliente.html")

#Pagina principal do cliente
def logado_view(request):
    context = {
        'pecas' : Peca.objects.all()
    }
    return render(request, "_paginas/logado.html", context)

def admin_login_view(request):
    return render(request, "_paginas/Admin_login.html")

def registro_view(request):
    return render(request, "_paginas/registro.html")

def registro_fixoa_view(request):
    return render(request,"_paginas/registro_clienteFixo.html")

def registro_fixob_view(request):
    return render(request,"_paginas/registro_clienteFixo2.html")

def carrinho_view(request):
    context = {
        'pcs' : PecaCarrinho.objects.all()
    }
    return render(request,"_paginas/finalizar.html", context)

def finalizar_view(request):
    c = Carrinho.objects.get(id=1)
    context = {
        'valor' : c.total
    }
    return render(request,"_paginas/finalizarCompra.html",context)

def finalizar_desconto_view(request):
    pc = PecaCarrinho.objects.all()
    c = Carrinho.objects.get(id=1)
    total = c.total
    for i in pc:
        if list(DescontoPeca.objects.filter(peca__id = i.peca.id))!=list(DescontoPeca.objects.none()):
            dp = DescontoPeca.objects.get(id=i.peca.id)
            total -= dp.desconto.valor * i.qtde
    
    context = {
        'valor' : total
    }
    return render(request,"_paginas/finalizarDesconto.html", context)

def consulta_avulso_view(request):
    return render(request, "_paginas/consultarClienteAvulso.html")

def consulta_fixo_view(request):
    return render(request, "_paginas/consultarClienteFixo.html")

def repositorio_view(request):
    context = {
        'pecas' : Peca.objects.all()
    }
    return render(request, "_paginas/repositorio.html", context)

def desconto_view(request):
    context = {
        'dps' : DescontoPeca.objects.all()
    }
    return render(request, "_paginas/descontos.html", context)

def adiciona_peca_view(request):
    form = PecaForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('repositorio')
    context = {
        'form' : form
    }
    return render(request,"_paginas/adicionarPeca.html", context)

def adiciona_desconto_view(request, id_peca):
    form = DescontoForm(request.POST)
    if list(DescontoPeca.objects.filter(peca__id = id_peca))==list(DescontoPeca.objects.none()):
        if form.is_valid():
            d = form.save()
            p = Peca.objects.get(id=id_peca)
            dp = DescontoPeca(peca=p,desconto=d)
            dp.save()
            return redirect('repositorio')
    else:
        return redirect('repositorio')
    
    context = {
        'form' : form
    }
    return render(request,"_paginas/adicionarDesconto.html", context)

def altera_desconto_view(request, id_desc):
    desc = Desconto.objects.get(id=id_desc)
    form = DescontoForm(request.POST, instance=desc)
    if form.is_valid():
        form.save()
        return redirect('descontos')

    context = {
        'form' : form
    }
    return render(request,"_paginas/atualizarDesconto.html", context)

def altera_peca_view(request, id_peca):
    peca = Peca.objects.get(id=id_peca)
    form = PecaForm(request.POST, instance=peca)
    if form.is_valid():
        form.save()
        return redirect('repositorio')

    context = {
        'form' : form
    }
    return render(request,"_paginas/atualizarPeca.html", context)

def altera_avulso_view(request):
    return render(request,"_paginas/atualizarClienteAvulso.html")

def altera_fixo_view(request):
    return render(request,"_paginas/atualizarClienteFixo.html")

def remove_peca(request, id_peca):
    Peca.objects.filter(id=id_peca).delete()
    return redirect('repositorio')

def remove_desc(request, id_desc):
    Desconto.objects.filter(id=id_desc).delete()
    return redirect('descontos')

def remove_cart(request, id_pc):
    pc = PecaCarrinho.objects.get(id=id_pc)
    pc.carrinho.total -= pc.peca.preco * pc.qtde
    pc.peca.estoque += pc.qtde
    pc.carrinho.save()
    pc.peca.save()
    pc.delete()
    return redirect('carrinho')

def adicionar_carrinho(request, id_peca):
    if list(PecaCarrinho.objects.filter(peca__id = id_peca))==list(PecaCarrinho.objects.none()):
        if list(Carrinho.objects.all())==list(Carrinho.objects.none()):
            c = Carrinho()
        else:
            c = Carrinho.objects.get(id=1)
        p = Peca.objects.get(id=id_peca)
        if p.estoque > 0:
            p.estoque -= 1
            c.total += p.preco
            pc = PecaCarrinho(peca=p, qtde=1, carrinho=c)
            p.save()
            c.save()
            pc.save()
            return redirect('logado')
        else:
            return redirect('logado')
    else:
        pc = PecaCarrinho.objects.get(peca__id = id_peca)
        if pc.peca.estoque > 0:
            pc.peca.estoque -= 1
            pc.qtde += 1
            pc.carrinho.total += pc.peca.preco
            pc.peca.save()
            pc.carrinho.save()
            pc.save()
            return redirect('logado')
        else:
            return redirect('logado')

def limpador(request, desc):
    c = Carrinho.objects.get(id=1)
    total = c.total
    c.total = 0
    c.save()
    if desc == 'n':
        pedido = Pedido(valor=total, desconto=False, data=datetime.now())
    else:
        pc = PecaCarrinho.objects.all()
        for i in pc:
            if list(DescontoPeca.objects.filter(peca__id = i.peca.id))!=list(DescontoPeca.objects.none()):
                dp = DescontoPeca.objects.get(i.peca.id)
                total -= dp.desconto.valor
        pedido = Pedido(valor=total, desconto=True, data=datetime.now())
    PecaCarrinho.objects.all().delete()
    pedido.save()
    return redirect('logado')