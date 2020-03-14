from django.contrib import admin
from .models import Contestant

# Register your models here.


class ContestantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'school', 'votes_total')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25


admin.site.register(Contestant, ContestantAdmin)
