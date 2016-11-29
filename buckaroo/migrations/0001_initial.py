# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-11-15 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=300)),
                ('website_key', models.CharField(max_length=300)),
                ('secret', models.CharField(max_length=300)),
                ('refund_fee', models.DecimalField(decimal_places=2, max_digits=5)),
                ('test_mode', models.BooleanField(default=True)),
                ('return_url', models.CharField(max_length=500)),
                ('refunds_enabled', models.BooleanField(default=False)),
                ('ember_base_path', models.CharField(max_length=500)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
