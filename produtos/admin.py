from django.contrib import admin
from django.utils.html import format_html
from .models import Produto, ListaPresente

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('preco','nome', 'link_afiliado', 'imagem')
    search_fields = ('nome', 'descricao')
    list_filter = ('preco',)
    ordering = ('nome',)
    
    def imagem(self, obj):
        if obj.imagem:
            return format_html('<img src="{}" width="50" height="50" />', obj.imagem.url)
        return "Sem imagem"

    imagem.short_description = 'Imagem do produto'


class ListaPresenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    filter_horizontal = ('produtos',)

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(ListaPresente, ListaPresenteAdmin)
