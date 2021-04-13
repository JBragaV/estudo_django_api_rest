from django.contrib import admin
from .models import Compras


class ComprasAdm(admin.ModelAdmin):
    list_display = ('id', 'produto', 'quantidade', 'data_incercao')
    list_display_links = ('id', 'produto')
    list_per_page = 10
    search_fields = ('produto',)


admin.site.register(Compras, ComprasAdm)
