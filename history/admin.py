from django.contrib import admin
from .models import History

class HistoryAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'id')

admin.site.register(History, HistoryAdmin)
