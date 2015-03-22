# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('filesAndForms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inputfile',
            name='next_one',
            field=models.FileField(upload_to='documents/%Y/%m/%d', default=datetime.datetime(2015, 3, 22, 19, 7, 57, 994147, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
