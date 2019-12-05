from django.shortcuts import render

# Create your views here.

def index_view(request):
    return render(request, "index.html")

def login_view(request):
    return render(request, "_paginas/logar.html")

def verifica_view(request):
    return render(request, "_paginas/verificadorCliente.html")

def logado_view(request):
    return render(request, "_paginas/logado.html")

def admin_login_view(request):
    return render(request, "_paginas/Admin_login.html")

def registro_view(request):
    return render(request, "_paginas/registro.html")

def registro_fixoa_view(request):
    return render(request,"_paginas/registro_clienteFixo.html")

def registro_fixob_view(request):
    return render(request,"_paginas/registro_clienteFixo2.html")

def carrinho_view(request):
    return render(request,"_paginas/finalizar.html")

def finalizar_view(request):
    return render(request,"_paginas/finalizarCompra.html")

def consulta_avulso_view(request):
    return render(request, "_paginas/consultarClienteAvulso.html")

def consulta_fixo_view(request):
    return render(request, "_paginas/consultarClienteFixo.html")

def repositorio_view(request):
    return render(request, "_paginas/repositorio.html")

def desconto_view(request):
    return render(request, "_paginas/descontos.html")

def adiciona_peca_view(request):
    return render(request,"_paginas/adicionarPeca.html")

def adiciona_desconto_view(request):
    return render(request,"_paginas/adicionarDesconto.html")

def altera_desconto_view(request):
    return render(request,"_paginas/atualizarDesconto.html")

def altera_peca_view(request):
    return render(request,"_paginas/atualizarPeca.html")

def altera_avulso_view(request):
    return render(request,"_paginas/atualizarClienteAvulso.html")

def altera_fixo_view(request):
    return render(request,"_paginas/atualizarClienteFixo.html")

