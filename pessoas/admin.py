from django.contrib import admin
from pessoas.models import Pessoas


class PessoasAdm(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cidade')
    list_display_links = ('id', 'nome')
    list_per_page = 10
    search_fields = ('nome', 'cidade')


admin.site.register(Pessoas, PessoasAdm)
