from django.urls import path
from .views import *

urlpatterns = [
    path('',index_view, name='index'),
    path('index/',index_view, name='index'),
    path('login/',login_view, name='login'),
    path('verificacao/',verifica_view, name='verificacao'),
    path('drjautopecas/',logado_view, name='logado'),
    path('drjadmin/',admin_login_view, name='admlogin'),
    path('cadastro/',registro_view, name='cadastro'),
    path('cadfixa/',registro_fixoa_view,name='fixoa'),
    path('cadfixb/',registro_fixob_view,name='fixob'),
    path('carrinho/',carrinho_view,name='carrinho'),
    path('finalizar/',finalizar_view,name='finalizar'),
    path('finalizar-desc/',finalizar_desconto_view,name='fimdesc'),
    path('consulta-avulso/',consulta_avulso_view,name='consulta-avulso'),
    path('consulta-fixo/',consulta_fixo_view,name='consulta-fixo'),
    path('repositorio/',repositorio_view,name='repositorio'),
    path('descontos/',desconto_view,name='descontos'),
    path('adicionar-peca/',adiciona_peca_view,name='addpeca'),
    path('adiciona-desconto/<int:id_peca>/',adiciona_desconto_view,name='adddscnt'),
    path('altera-desconto/<int:id_desc>/',altera_desconto_view,name='altdscnt'),
    path('altera-peca/<int:id_peca>/',altera_peca_view,name='altpeca'),
    path('altera-avulso/',altera_avulso_view,name='altavulso'),
    path('altera-fixo/',altera_fixo_view,name='altfixo'),
    path('rem-peca/<int:id_peca>/',remove_peca,name='rempeca'),
    path('rem-desc/<int:id_desc>/',remove_desc,name='remdesc'),
    path('rem-cart/<int:id_pc>/',remove_cart,name='remcart'),
    path('addcart/<int:id_peca>/', adicionar_carrinho, name='addtocart'),
    path('limpando/<str:desc>/', limpador, name='limpeza')
]