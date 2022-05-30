from django.db import models

# Create your models here.

class user_DB(models.Model):
    name = models.CharField(max_length=1000)
    username = models.CharField(max_length=1000)
    phone_number =models.CharField(max_length=11)


class events_DB(models.Model):
    username=models.CharField(max_length=100)
    name = models.CharField(max_length=1000)
    desc = models.TextField()
    venue = models.CharField(max_length=1000)
    time = models.CharField(max_length=100)
    verified = models.BooleanField(default=False)
    price = models.CharField(max_length=1000)
    model_image=models.ImageField(blank=True,upload_to='event_images/')
   

class booked_DB(models.Model):
    username = models.CharField(max_length=1000)
    event_name = models.CharField(max_length=100)
    number=models.CharField(max_length=100)
    tprice =models.CharField(max_length=100)



