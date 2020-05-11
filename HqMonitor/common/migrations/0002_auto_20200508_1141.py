# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-05-08 03:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compinfo',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='compinfo',
            name='name',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='compinfo',
            name='phone',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='comp_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='phone',
            field=models.CharField(max_length=16, null=True),
        ),
    ]
