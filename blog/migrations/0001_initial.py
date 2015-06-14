# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('title', models.CharField(max_length=255, verbose_name=b'Blog title')),
                ('slug', models.SlugField(max_length=255, serialize=False, verbose_name=b'Slug (unique)', primary_key=True)),
                ('description', models.CharField(max_length=255, verbose_name=b'Description (optional)', blank=True)),
                ('tags', models.CharField(max_length=150, verbose_name=b'Tags (Comma separated)', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Creation date')),
                ('published', models.BooleanField(default=True, verbose_name=b'Published')),
                ('content', models.TextField()),
                ('content_processed', models.TextField()),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
