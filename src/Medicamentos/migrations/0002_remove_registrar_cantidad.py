# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-28 15:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Medicamentos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrar',
            name='Cantidad',
        ),
    ]
