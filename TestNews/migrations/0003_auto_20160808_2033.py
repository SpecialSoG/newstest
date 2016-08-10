# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TestNews', '0002_auto_20160807_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(verbose_name='Картинка', upload_to='111/', null=True, blank=True),
        ),
    ]
