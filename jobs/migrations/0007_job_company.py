# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-10-09 18:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_job_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='company',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
