# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 12:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('callback_url', models.URLField(blank=True, null=True)),
                ('img_url', models.URLField(default='http://bizhi.zhuoku.com/2013/06/21/zhuoku/zhuoku123.jpg')),
                ('description', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'verbose_name': '\u9996\u9875\u5927\u56fe',
                'verbose_name_plural': '\u9996\u9875\u5927\u56fe',
            },
        ),
    ]