# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-29 20:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Doctores', '0005_auto_20170429_2047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itinerario',
            old_name='idFamilia',
            new_name='idMedicamento',
        ),
    ]