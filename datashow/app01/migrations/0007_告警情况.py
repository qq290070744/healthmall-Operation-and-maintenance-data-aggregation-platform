# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-12 17:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_当前的ha访问量'),
    ]

    operations = [
        migrations.CreateModel(
            name='告警情况',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alerttypeId', models.IntegerField()),
                ('alerttype', models.CharField(max_length=100)),
                ('alertNum', models.IntegerField()),
            ],
        ),
    ]
