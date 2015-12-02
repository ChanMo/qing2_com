from django.contrib import admin
from .models import Type, Theme, Template

class TypeAdmin(admin.ModelAdmin):
    pass

class TemplateInline(admin.TabularInline):
    model = Template
    extra = 3

class ThemeAdmin(admin.ModelAdmin):
    list_display = ('type', 'name', 'rendering_url', 'description', 'created')
    inlines = [TemplateInline]

admin.site.register(Type, TypeAdmin)
admin.site.register(Theme, ThemeAdmin)
