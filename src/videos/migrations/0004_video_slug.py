# Generated by Django 2.1.7 on 2019-03-23 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_video_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
