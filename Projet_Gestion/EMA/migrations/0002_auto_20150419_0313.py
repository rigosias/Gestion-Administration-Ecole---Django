# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EMA', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eleve',
            name='no_Dossier',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
