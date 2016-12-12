# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-12 16:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('secret_key', models.CharField(max_length=6)),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='giftee',
            field=models.ForeignKey(db_column='giftee_id', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='secretsanta.Person'),
        ),
        migrations.AddField(
            model_name='match',
            name='gifter',
            field=models.ForeignKey(db_column='gifter_id', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='secretsanta.Person'),
        ),
    ]
