# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galerias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=100)),
                ('msg', models.CharField(max_length=2048)),
                ('date', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='urls',
            name='description',
            field=models.CharField(default=' ', max_length=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='urls',
            name='title',
            field=models.CharField(default=' ', max_length=250),
            preserve_default=False,
        ),
    ]
