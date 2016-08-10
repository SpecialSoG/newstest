# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TestNews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(verbose_name='Image', null=True, upload_to='images/', blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(max_length=160),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=160),
        ),
    ]
