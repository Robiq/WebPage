# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 04:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='name',
            new_name='path',
        ),
    ]
