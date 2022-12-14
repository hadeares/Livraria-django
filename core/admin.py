from django.contrib import admin

from core.models import Autor, Categoria, Editora, Livros, Compra, ItensCompra

admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Livros)



class ItensInLine(admin.TabularInline):
    model = ItensCompra

@admin.register(Compra)
class CompraAdimin(admin.ModelAdmin):
    inlines = (ItensInLine,)