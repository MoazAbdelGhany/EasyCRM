from django.contrib import admin
from .models import *
from django.forms import TextInput

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == "phone":
            kwargs['widget'] = TextInput(attrs={'size':'11'})
        return super().formfield_for_dbfield(db_field, request, **kwargs)