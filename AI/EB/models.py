from django.db import models

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=100)
    time = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    powerRating = models.IntegerField(default=0)
    onTime = models.IntegerField(default=0)    
    