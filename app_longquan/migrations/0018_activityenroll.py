# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-15 19:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_longquan', '0017_activityschedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityEnroll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=60)),
                ('lunch', models.CharField(max_length=10)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_enroll', to='app_longquan.Activity')),
            ],
        ),
    ]