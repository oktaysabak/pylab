# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2019-05-17 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_postmodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='title',
            field=models.CharField(error_messages={'unique': 'Ayni baslikta baska kayit olamaz'}, max_length=240, unique=True, verbose_name='Post Title'),
        ),
    ]