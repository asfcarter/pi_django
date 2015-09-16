# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pi_django_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pi_django_app',
            name='full_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
