# Generated by Django 3.2.19 on 2023-10-06 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exploreApp', '0009_alter_explore_place_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='explore_place',
            name='image',
            field=models.CharField(max_length=500),
        ),
    ]