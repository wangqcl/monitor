# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-05-07 09:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_name', models.CharField(max_length=16)),
                ('address', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=16)),
                ('phone', models.CharField(max_length=16)),
                ('comp_ip', models.CharField(max_length=32)),
                ('comp_realm', models.CharField(max_length=32)),
                ('addtime', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'compinfo',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=32)),
                ('sex', models.IntegerField(default=1)),
                ('phone', models.CharField(max_length=16)),
                ('email', models.CharField(max_length=50)),
                ('state', models.IntegerField(default=1)),
                ('comp_id', models.IntegerField()),
                ('addtime', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]