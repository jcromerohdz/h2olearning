# Generated by Django 2.1.7 on 2019-04-17 22:00

import courses.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20190417_2140'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lecture',
            options={'ordering': ['order', 'title']},
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=courses.fields.PositionField(default=-1),
        ),
    ]