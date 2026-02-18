from django.contrib import admin
from apps.base.models import Settings
# Register your models here.

@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('title', 'phone_number')
    search_fields = ('title', 'phone_number')
    fieldsets = (
        ('Основные информации', {
            'fields': ('title', 'logo', 'icon', 'description')
        }),
        ('Контактные данные', {
            'fields': ('address', 'locate', 'phone_number', 'email')
        }),
        ('Соц. сети', {
            'fields': ('instagram', 'facebook', 'youtube', 'whatsapp', 'telegram'),
            'classes': ('collapse',)
        })
    )