# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-19 04:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroDoctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(blank=True, max_length=8)),
                ('direccion', models.CharField(max_length=60)),
                ('especialidad', models.CharField(blank=True, max_length=8)),
            ],
        ),
    ]