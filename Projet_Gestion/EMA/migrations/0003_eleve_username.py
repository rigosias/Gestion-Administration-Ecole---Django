# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EMA', '0002_auto_20150419_0313'),
    ]

    operations = [
        migrations.AddField(
            model_name='eleve',
            name='username',
            field=models.CharField(default=b'string', max_length=20),
            preserve_default=True,
        ),
    ]
