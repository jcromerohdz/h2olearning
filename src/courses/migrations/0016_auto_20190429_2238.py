# Generated by Django 2.2 on 2019-04-29 22:38

import courses.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_course_secondary'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, height_field=models.IntegerField(blank=True, null=True), null=True, upload_to=courses.models.handle_upload, width_field=models.IntegerField(blank=True, null=True)),
        ),
        migrations.AddField(
            model_name='course',
            name='image_height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='image_width',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
