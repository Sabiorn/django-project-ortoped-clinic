from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена, руб.')

    # image = models.ImageField(upload_to='service_images/')
    # Другие поля, такие как описание, цена, изображение и т. д., могут быть добавлены по необходимости
    class Meta:
        db_table = 'Service'
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы'

    def __str__(self):
        return self.name


