# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-17 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boi', '0003_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mercadoria',
            name='nome',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='mercadoria',
            name='tipo_mercadoria',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='mercadoria',
            name='tipo_negocio',
            field=models.CharField(blank=True, choices=[('Person', 'Person'), ('Group', 'Group'), ('Other', 'Other')], max_length=20, null=True),
        ),
    ]
