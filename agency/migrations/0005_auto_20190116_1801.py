# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-16 15:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0004_auto_20190116_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='gender',
            field=models.CharField(choices=[('FEMALE', 'FEMALE'), ('MALE', 'MALE')], max_length=7),
        ),
    ]
