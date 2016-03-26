# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 08:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('classifytag', models.CharField(max_length=30)),
                ('text', models.TextField()),
                ('pub_time', models.DateTimeField()),
                ('mod_time', models.DateTimeField()),
            ],
        ),
    ]