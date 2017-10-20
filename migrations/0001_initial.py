# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97')),
                ('avar', models.ImageField(upload_to=b'uploads/%Y/%m/%d', verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f')),
            ],
        ),
    ]
