# Generated by Django 5.0.1 on 2024-02-20 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0010_categories_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Услуга', 'verbose_name_plural': 'Услуги'},
        ),
        migrations.AlterField(
            model_name='categories',
            name='description',
            field=models.TextField(blank=True, max_length=1500, verbose_name='Описание'),
        ),
    ]
