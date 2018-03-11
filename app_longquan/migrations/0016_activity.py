# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-14 20:04
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_longquan', '0015_auto_20170627_1830'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('activity_title', models.CharField(max_length=200, primary_key=True, serialize=False, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('activity_location', models.CharField(default=b'\xe5\xbf\x85\xe5\xa1\xab', max_length=100, verbose_name=b'\xe5\x9c\xb0\xe7\x82\xb9')),
                ('activity_date', models.DateTimeField(verbose_name=b'\xe6\xb4\xbb\xe5\x8a\xa8\xe6\x97\xa5\xe6\x9c\x9f')),
                ('activity_description', models.TextField(default=b'\xe5\xbf\x85\xe5\xa1\xab', max_length=2000, verbose_name=b'\xe5\x86\x85\xe5\xae\xb9\xe7\xae\x80\xe4\xbb\x8b')),
                ('activity_content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name=b'\xe5\x8f\xaf\xe9\x80\x89')),
                ('activity_photo', models.ImageField(default=b'\xe5\x8f\xaf\xe9\x80\x89', upload_to=b'activities/', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87')),
                ('activity_source', models.TextField(default=b'\xe5\x8f\xaf\xe9\x80\x89', max_length=2000, verbose_name=b'\xe4\xbf\xa1\xe6\x81\xaf\xe6\x9d\xa5\xe6\xba\x90')),
                ('activity_publisher', models.CharField(default=b'\xe5\x8f\xaf\xe9\x80\x89', max_length=100, verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe8\x80\x85')),
                ('activity_publish_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xa5\xe6\x9c\x9f')),
                ('activity_column', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity', to='app_longquan.Column')),
            ],
        ),
    ]