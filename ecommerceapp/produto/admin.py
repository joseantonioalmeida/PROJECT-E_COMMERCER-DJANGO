from django.contrib import admin
from produto.models import Produto, Variacao

# Register your models here.


class VariacaoInline(admin.TabularInline):
    model = Variacao
    extra = 1
    

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):    
    list_display = ('nome', 'descricao_curta', 'get_preco_formatado', 'get_preco_promocional')
    search_fields = ('nome', 'descricao_curta')
    inlines = [
        VariacaoInline,
    ]

@admin.register(Variacao)
class VariacaoAdmin(admin.ModelAdmin):    
    list_display = ('nome', 'produto')
    search_fields = ('nome', 'produto')