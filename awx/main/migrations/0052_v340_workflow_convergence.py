# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-09-28 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0051_v340_job_slicing'),
    ]

    operations = [
        migrations.AddField(
            model_name='workflowjobnode',
            name='do_not_run',
            field=models.BooleanField(default=False),
        ),
    ]