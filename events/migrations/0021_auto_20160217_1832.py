# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-17 16:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0020_image_name'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='eventlink',
            unique_together=set([('name', 'event', 'language', 'link')]),
        ),
    ]
