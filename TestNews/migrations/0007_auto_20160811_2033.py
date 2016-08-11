# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TestNews', '0006_auto_20160810_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(verbose_name='Image', upload_to='images/', blank=True, null=True),
        ),
    ]
