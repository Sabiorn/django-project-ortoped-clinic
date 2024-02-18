from django.contrib import admin
from goods.models import Staff
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


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug']  # Добавляем 'slug' в список отображаемых полей
    search_fields = ['name']
    fields = [
        'name',
        'description',
        'image',
        'slug',  # Включаем поле 'slug' в административный интерфейс
    ]
    class Meta:
        db_table = 'Staff'
        verbose_name = 'Персонал'
        verbose_name_plural = 'Персонал'
