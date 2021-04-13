from django.contrib import admin
from .models import Livros


class LivrosAdm(admin.ModelAdmin):
    list_display = ('id', 'nome', 'tema', 'emprestado', 'pessoas')
    list_display_links = ('id', 'nome')
    list_per_page = 10
    search_fields = ('nome', 'tema')


admin.site.register(Livros, LivrosAdm)
