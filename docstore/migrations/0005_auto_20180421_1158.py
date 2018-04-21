# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-21 06:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('docstore', '0004_auto_20180421_0830'),
    ]

    operations = [
        migrations.AddField(
            model_name='artifact',
            name='remark',
            field=models.CharField(default=datetime.datetime(2018, 4, 21, 6, 28, 2, 620753, tzinfo=utc), max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='artifact',
            name='docname',
            field=models.CharField(max_length=100),
        ),
    ]