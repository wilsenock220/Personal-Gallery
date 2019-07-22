# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-22 05:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['image_name']},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='Name',
            new_name='category_name',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='Name',
            new_name='image_name',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='place',
            new_name='location_name',
        ),
        migrations.RemoveField(
            model_name='image',
            name='description',
        ),
        migrations.RemoveField(
            model_name='image',
            name='submited',
        ),
        migrations.AddField(
            model_name='image',
            name='image_description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.Category'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='imgs/'),
        ),
    ]
