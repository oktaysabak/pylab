# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2019-05-17 11:40
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_postmodel_author_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='author_email',
            field=models.CharField(blank=True, max_length=240, null=True, validators=[blog.models.validate_author_email]),
        ),
    ]
