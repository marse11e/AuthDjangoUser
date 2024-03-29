# Generated by Django 5.0.2 on 2024-02-29 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_customuser_location_customuser_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='latitude',
            field=models.CharField(blank=True, help_text='Широта пользователя в Telegram.', max_length=120, null=True, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='longitude',
            field=models.CharField(blank=True, help_text='Долгота пользователя в Telegram.', max_length=120, null=True, verbose_name='Долгота'),
        ),
    ]
