# Generated by Django 3.2.19 on 2023-10-13 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exploreHotels', '0006_remove_hotels_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='city',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]
