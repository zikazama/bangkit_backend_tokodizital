from django.contrib import admin
from disease.models import Disease

#filter horizontal

class DiseaseAdmin(admin.ModelAdmin):
    filter_horizontal = ('products',)
    list_display = ('name', 'created_at', 'updated_at')

admin.site.register(Disease, DiseaseAdmin)