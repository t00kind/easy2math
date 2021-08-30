from django.contrib import admin
from .models import Ll, Level

class LAdmin(admin.ModelAdmin):
    list_display = ('url', 'level')
    list_display_links = ('url', 'level')
    search_fields = ('url', 'level')

admin.site.register(Ll, LAdmin)
admin.site.register(Level)