# Generated by Django 4.0.5 on 2022-06-13 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_video_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='isProcessed',
            field=models.BooleanField(default=False),
        ),
    ]
