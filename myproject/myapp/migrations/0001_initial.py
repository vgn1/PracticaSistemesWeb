# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('birthday', models.DateField()),
                ('biography', models.TextField(null=True, blank=True)),
                ('user', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.PositiveSmallIntegerField(default=0, verbose_name=b'Category', choices=[(0, b'Undefined'), (1, b'Thriller'), (2, b'Comedy'), (3, b'Terror'), (4, b'Action'), (5, b'Romantic'), (6, b'Adventure'), (7, b'Sci-fi'), (8, b'Drama'), (9, b'Western'), (10, b'Animation')])),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('homePage', models.TextField(null=True, blank=True)),
                ('user', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('birthday', models.DateField()),
                ('biography', models.TextField(null=True, blank=True)),
                ('user', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('year', models.IntegerField()),
                ('overview', models.TextField(null=True, blank=True)),
                ('director', models.ForeignKey(to='myapp.Director')),
                ('user', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.PositiveSmallIntegerField(default=0, verbose_name=b'Rating (stars)', choices=[(0, b'Undefined'), (1, b'one'), (2, b'two'), (3, b'three'), (4, b'four'), (5, b'five')])),
                ('comment', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ternary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actor', models.ForeignKey(to='myapp.Actor')),
                ('company', models.ForeignKey(to='myapp.Company')),
                ('movie', models.ForeignKey(to='myapp.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='MovieCategory',
            fields=[
                ('category_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='myapp.Category')),
                ('movie', models.ForeignKey(to='myapp.Movie')),
            ],
            bases=('myapp.category',),
        ),
        migrations.CreateModel(
            name='MovieReview',
            fields=[
                ('review_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='myapp.Review')),
                ('movies', models.ForeignKey(to='myapp.Movie')),
            ],
            bases=('myapp.review',),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='category',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
    ]
