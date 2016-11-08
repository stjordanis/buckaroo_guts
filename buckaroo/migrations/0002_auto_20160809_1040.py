# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-09 08:40
from __future__ import unicode_literals

from django.db import migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('buckaroo', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BuckarooTransactionStatus',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=django_fsm.FSMField(default='new', max_length=50, protected=True),
        ),
    ]