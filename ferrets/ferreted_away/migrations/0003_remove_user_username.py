# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 11:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ferreted_away', '0002_auto_20170314_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
