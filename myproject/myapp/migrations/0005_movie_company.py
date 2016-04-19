# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20160417_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='company',
            field=models.ManyToManyField(to='myapp.Company'),
        ),
    ]
