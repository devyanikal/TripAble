from django.db import models


# Create your models here.

class Explore_place(models.Model):
    place_id=models.AutoField(primary_key=True)
    place_name=models.CharField(max_length=100)
    visual_impaired=models.BooleanField()
    wheelchair_user=models.BooleanField()
    hearing_impaired=models.BooleanField()
    speech_impaired=models.BooleanField()
    city=models.CharField(max_length=100)
    facility=models.TextField()
    About=models.TextField()
    location=models.CharField(max_length=500)
    # image=models.ImageField(upload_to='files/places')