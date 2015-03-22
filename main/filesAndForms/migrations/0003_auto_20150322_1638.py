# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('filesAndForms', '0002_inputfile_next_one'),
    ]

    operations = [
        migrations.AddField(
            model_name='inputfile',
            name='name',
            field=models.CharField(default=datetime.datetime(2015, 3, 22, 20, 38, 56, 580815, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inputfile',
            name='privacy',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
