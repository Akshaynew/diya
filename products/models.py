from django.db import models

# Create your models here.
class items(models.Model):
    name=models.CharField(max_length=255)
    subname=models.CharField(max_length=1000)
    price=models.FloatField()
    stock=models.IntegerField()
    image=models.CharField(max_length=2500)
