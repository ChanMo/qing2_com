# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0002_auto_20151123_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='latitude',
            field=models.DecimalField(max_digits=13, decimal_places=10),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='longitude',
            field=models.DecimalField(max_digits=14, decimal_places=10),
        ),
    ]
