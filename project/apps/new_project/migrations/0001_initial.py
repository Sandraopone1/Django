# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-27 04:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='schedules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='trip',
            name='plannedby',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new_project.User'),
        ),
        migrations.AddField(
            model_name='schedules',
            name='the_traveller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new_project.User'),
        ),
        migrations.AddField(
            model_name='schedules',
            name='the_trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new_project.Trip'),
        ),
    ]
