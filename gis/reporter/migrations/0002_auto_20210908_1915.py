# Generated by Django 3.2.6 on 2021-09-08 18:15

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='incidences',
            options={'verbose_name_plural': 'Incidences'},
        ),
        migrations.AlterField(
            model_name='incidences',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326),
        ),
    ]