from django.urls import path, include
from produto import views


app_name = 'produto'
 
urlpatterns = [
    path('', views.ListaProdutos.as_view(),name='lista'),
    path('adicionaraocarrinho/', views.AdicionarAoCarrinho.as_view(),name='adicionaraocarrinho'),
    path('removerdocarrinho/', views.RemoverDoCarinho.as_view(),name='removerdocarrinho'),
    path('carrinho/', views.Carrinho.as_view(),name='carrinho'),
    path('finalizar/', views.Finalizar.as_view(),name='finalizar'),
    path('<slug>/', views.DetalheProduto.as_view(),name='detalhe'),
]