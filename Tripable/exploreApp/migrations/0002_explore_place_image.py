# Generated by Django 3.2.19 on 2023-10-02 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exploreApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='explore_place',
            name='image',
            field=models.ImageField(default=None, upload_to='files/places'),
        ),
    ]
