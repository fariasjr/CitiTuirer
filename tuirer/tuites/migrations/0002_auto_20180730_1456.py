# Generated by Django 2.0.7 on 2018-07-30 17:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuites', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tuite',
            options={'ordering': ('content',)},
        ),
        migrations.AlterField(
            model_name='tuite',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tuites', to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='tuite',
            name='content',
            field=models.CharField(default='Olá!', max_length=280, verbose_name='Tuite'),
        ),
    ]
