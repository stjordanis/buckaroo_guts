# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-16 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buckaroo', '0004_transaction_payment_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='buckaroo_push',
            field=models.BooleanField(default=False),
        ),
    ]
