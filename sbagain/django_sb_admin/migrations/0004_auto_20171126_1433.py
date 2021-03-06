# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-26 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_sb_admin', '0003_auto_20171112_0617'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=255, unique=True)),
                ('host', models.CharField(max_length=255)),
                ('hostname', models.CharField(max_length=255)),
                ('host_vars', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'inventory',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='hostinfo',
            options={'managed': False},
        ),
    ]
