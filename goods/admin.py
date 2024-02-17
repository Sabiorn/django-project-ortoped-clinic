from django.contrib import admin

from goods.models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name']
    fields = [
        'name',
        'price',
    ]
    class Meta:
        db_table = 'services'
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы'
