# Generated by Django 2.2 on 2019-04-29 22:38

import courses.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0016_auto_20190429_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, height_field='image_height', null=True, upload_to=courses.models.handle_upload, width_field='image_width'),
        ),
    ]
