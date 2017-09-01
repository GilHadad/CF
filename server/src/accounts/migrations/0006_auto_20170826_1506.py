# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-08-26 12:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20170825_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='lead_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Company', to='accounts.Team'),
        ),
        migrations.AlterField(
            model_name='teamtree',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ParentTeam', to='accounts.Team'),
        ),
    ]
