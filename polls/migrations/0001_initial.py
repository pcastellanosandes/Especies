# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-02-07 06:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Specie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photoPath', models.CharField(max_length=1000)),
            ],
        ),
    ]