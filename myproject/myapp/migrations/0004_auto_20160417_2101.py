# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_movie_companies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviecategory',
            name='movie',
            field=models.ForeignKey(related_name='cat', to='myapp.Movie'),
        ),
        migrations.AlterField(
            model_name='moviereview',
            name='movies',
            field=models.ForeignKey(related_name='rate', to='myapp.Movie'),
        ),
    ]
