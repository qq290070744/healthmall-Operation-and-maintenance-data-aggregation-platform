# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-14 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0019_auto_20170713_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='redis命中率',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('电商命中率', models.CharField(max_length=100)),
                ('NET命中率', models.CharField(max_length=100)),
                ('SSO命中率', models.CharField(max_length=100)),
                ('times', models.CharField(max_length=100)),
            ],
        ),
    ]
