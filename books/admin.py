from django.contrib import admin
from .models import Books, Level

class BkAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'pdf', 'published', 'level', 'epub', 'fb2', 'mobi')
    list_display_links = ('title', 'fb2', 'pdf', 'epub', 'mobi')
    searc_fields = ('title', 'description')

admin.site.register(Books, BkAdmin)
admin.site.register(Level)
