from django.contrib import admin
from .models import Tt, Level

class TtAdmin(admin.ModelAdmin):
    list_display = ('level',)
    list_display_links = ('level',)
    searc_fields = ('level',)

admin.site.register(Tt, TtAdmin)
admin.site.register(Level)
