# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('royal', '0004_deck'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rarity', models.CharField(default='None', max_length=20)),
                ('typeof', models.CharField(default='None', max_length=20)),
                ('elixir', models.IntegerField(default=0)),
                ('arena', models.IntegerField(default=-1)),
            ],
        ),
    ]
