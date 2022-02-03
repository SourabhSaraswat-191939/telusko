from django.db import models

# Create your models here.

# class Destination:
#     id: int
#     name: str
#     img: str
#     desc: str
#     price: int
#     offer : bool

#upward code is of class but we need model to communicate with database. So to make model use  below method :

class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)