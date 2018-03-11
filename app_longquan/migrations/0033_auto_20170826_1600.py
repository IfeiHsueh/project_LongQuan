# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-26 14:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_longquan', '0032_auto_20170826_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='InspirationColumn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_name', models.CharField(max_length=256, verbose_name=b'\xe6\xa0\x8f\xe7\x9b\xae\xe5\x90\x8d\xe7\xa7\xb0')),
            ],
        ),
        migrations.AddField(
            model_name='inspiration',
            name='column',
            field=models.ForeignKey(default=b'', on_delete=django.db.models.deletion.CASCADE, related_name='inspiration', to='app_longquan.InspirationColumn', verbose_name=b'\xe6\xa0\x8f\xe7\x9b\xae\xe5\x90\x8d\xe7\xa7\xb0\xef\xbc\x88\xe5\xbf\x85\xe9\x80\x89\xef\xbc\x89'),
        ),
    ]