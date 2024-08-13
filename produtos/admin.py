from django.contrib import admin
from .models import Produto, ListaPresente
from django.utils.translation import gettext_lazy as _

admin.site.site_header = _("Administração da Papelzinho Store")
admin.site.site_title = _("Papelzinho Store")
admin.site.index_title = _("Bem-vindo ao Painel de Administração")

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'link_afiliado')  # Exibir essas colunas na lista
    search_fields = ('nome', 'descricao')  # Adicionar barra de busca
    list_filter = ('preco',)  # Adicionar filtros laterais
    ordering = ('nome',)  # Ordenar por nome

    # Customizar a visualização dos campos no formulário de edição
    fieldsets = (
        (None, {
            'fields': ('nome', 'descricao', 'preco', 'link_afiliado', 'imagem')
        }),
    )
    def imagem(self, obj):
        if obj.imagem:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.imagem.url))
        return "Sem imagem"

    imagem.short_description = 'Imagem'

class ListaPresenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    filter_horizontal = ('produtos',)  # Facilitar a seleção de produtos

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(ListaPresente, ListaPresenteAdmin)