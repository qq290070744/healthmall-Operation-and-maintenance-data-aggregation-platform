# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-13 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0017_网络情况_上海网络可用性'),
    ]

    operations = [
        migrations.AddField(
            model_name='网络情况',
            name='广州网络可用性',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
