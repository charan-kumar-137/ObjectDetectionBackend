# Generated by Django 3.2.13 on 2022-06-14 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='processed_image',
            field=models.ImageField(null=True, upload_to='images/processed/%d_%m_%Y'),
        ),
    ]
