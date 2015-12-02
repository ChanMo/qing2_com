# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apartment',
            old_name='created',
            new_name='is_true',
        ),
    ]
