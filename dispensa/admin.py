from django.contrib import admin

from dispensa.models import Dispensa
# Register your models here.


class DispensaAdm(admin.ModelAdmin):
    list_display = ('id', 'nome_produto', 'quantidade')
    list_display_links = ('id', 'nome_produto')
    search_fields = ('nome_produto',)
    list_per_page = 10


admin.site.register(Dispensa, DispensaAdm)
