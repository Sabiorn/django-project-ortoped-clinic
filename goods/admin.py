from django.contrib import admin
from goods.models import Categories, Staff
from goods.models import Service

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'description']

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
    search_fields = ['name']
    list_filter = ['category']
    fields = [
        'name',
        'price',
        'category',
    ]

    class Meta:
        db_table = 'services'
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы'

admin.site.register(Service, ServiceAdmin)



@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'job', 'category']  # Добавляем 'slug' в список отображаемых полей
    search_fields = ['name', 'category']
    fields = [
        'name',
        'description',
        'image',
        'job',
        'category'  # Включаем поле 'slug' в административный интерфейс
    ]
    class Meta:
        db_table = 'Staff'
        verbose_name = 'Персонал'
        verbose_name_plural = 'Персонал'
