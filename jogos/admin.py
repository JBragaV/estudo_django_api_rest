from django.contrib import admin
from .models import Jogos


class JogosAdm(admin.ModelAdmin):
    list_display = ('id', 'nome',
                    'plataforma', 'emprestado',
                    'data_emprestimo', 'pessoa')
    list_display_links = ('id', 'nome')
    list_per_page = 10
    search_fields = ('nome', 'plataforma')


admin.site.register(Jogos, JogosAdm)
