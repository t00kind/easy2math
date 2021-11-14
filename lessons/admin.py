from django.contrib import admin
from .models import Lessons, Tag

class LAdmin(admin.ModelAdmin):
    list_display = ('url', 'tag')
    list_display_links = ('url', 'tag')
    search_fields = ('url', 'tag')

admin.site.register(Lessons, LAdmin)
admin.site.register(Tag)