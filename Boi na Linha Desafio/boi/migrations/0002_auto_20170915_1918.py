# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-15 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mercadoria',
            name='codigo',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='mercadoria',
            name='quantidade',
            field=models.IntegerField(),
        ),
    ]
