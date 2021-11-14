from django.contrib import admin
from .models import Task

class TtAdmin(admin.ModelAdmin):
    list_display = ('task',)
    list_display_links = ('task',)
    searc_fields = ('task',)

admin.site.register(Task, TtAdmin)
 