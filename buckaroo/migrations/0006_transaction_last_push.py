# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-16 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buckaroo', '0005_transaction_buckaroo_push'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='last_push',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
