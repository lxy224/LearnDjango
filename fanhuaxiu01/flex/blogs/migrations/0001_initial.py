# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='tile of article')),
                ('writer', models.CharField(max_length=50, verbose_name='author of article')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('modify_date', models.DateField(auto_now=True)),
                ('content', models.TextField()),
                ('is_show', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Article',
            },
        ),
    ]
