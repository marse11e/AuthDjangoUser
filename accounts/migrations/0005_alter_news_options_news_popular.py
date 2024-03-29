# Generated by Django 5.0.2 on 2024-03-05 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_news'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-created_at'], 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AddField(
            model_name='news',
            name='popular',
            field=models.BooleanField(default=False, help_text='Указывает, является ли новость популярной.', verbose_name='Популярная'),
        ),
    ]
