# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_auto_20171030_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='tag',
            field=models.CharField(choices=[('pr', 'Preview'), ('na', 'Nature'), ('pe', 'People'), ('ur', 'Urban'), ('ot', 'Other')], max_length=2),
        ),
    ]