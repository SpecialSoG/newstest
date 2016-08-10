# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TestNews', '0004_auto_20160808_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(verbose_name='Картинка', blank=True, upload_to='111/', null=True),
        ),
    ]
