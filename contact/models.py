from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.subject
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    itag = models.CharField(max_length=200)
    image = models.ImageField(default='ittrain.png', upload_to='service')
    def __str__(self):
        return self.name

class Review(models.Model):
    name = models.CharField(max_length=100)
    Org = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/',null=True)
    itag = models.CharField(max_length=200)
    approve =  models.BooleanField(default=False) 
    def __str__(self):
        return self.name