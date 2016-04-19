# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ternary',
            name='actor',
        ),
        migrations.RemoveField(
            model_name='ternary',
            name='company',
        ),
        migrations.RemoveField(
            model_name='ternary',
            name='movie',
        ),
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(to='myapp.Actor'),
        ),
        migrations.AddField(
            model_name='movie',
            name='companies',
            field=models.ManyToManyField(to='myapp.Company'),
        ),
        migrations.DeleteModel(
            name='Ternary',
        ),
    ]
