# Generated by Django 2.1.7 on 2019-04-17 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20190417_2004'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lecture',
            options={'ordering': ['-order', '-title']},
        ),
        migrations.AddField(
            model_name='lecture',
            name='order',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]