# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-05 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='description',
            field=models.CharField(max_length=40),
        ),
    ]
