# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ferreted_away', '0002_item_itemid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='picture',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
    ]
