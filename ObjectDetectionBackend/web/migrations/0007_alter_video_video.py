# Generated by Django 3.2.13 on 2022-06-18 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_video_processed_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to='videos/'),
        ),
    ]
