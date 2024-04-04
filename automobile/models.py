from django.db import models

# Create your models here.
class Details(models.Model):
    sno = models.TextField()
    cname =  models.TextField()
    model =  models.TextField()
    img =  models.ImageField(upload_to='media/gallery_picture')
    price = models.TextField()
    engine =  models.TextField()
    power =  models.TextField()
    torque =  models.TextField()
    clearence =  models.TextField()
    mileage =  models.TextField()
    tank =  models.TextField()
    gearbox =  models.TextField()
    height =  models.TextField()
    length =  models.TextField()
    width =  models.TextField()
    weight =  models.TextField()
    wheelbase =  models.TextField()