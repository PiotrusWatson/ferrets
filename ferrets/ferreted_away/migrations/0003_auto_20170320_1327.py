# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ferreted_away', '0002_auto_20170317_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.TextField(max_length=360),
        ),
    ]