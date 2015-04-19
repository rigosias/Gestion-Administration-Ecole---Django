# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eleve',
            fields=[
                ('id_Eleve', models.AutoField(serialize=False, primary_key=True)),
                ('no_Dossier', models.CharField(max_length=100)),
                ('nom', models.CharField(max_length=10)),
                ('prenom', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id_Matiere', models.AutoField(serialize=False, primary_key=True)),
                ('nom_Matiere', models.CharField(max_length=100)),
                ('coefficient', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id_Note', models.AutoField(serialize=False, primary_key=True)),
                ('note_Eleve', models.FloatField(max_length=5)),
                ('coef', models.ForeignKey(to='EMA.Matiere')),
                ('id_el_note', models.ForeignKey(to='EMA.Eleve')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
