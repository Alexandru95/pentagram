# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 07:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Pentagram', '0008_auto_20160719_1030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='user',
            new_name='user_id',
        ),
    ]
