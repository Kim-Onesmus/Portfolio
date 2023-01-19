from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'media/')
    
    def __str__(self):
        return (self.name)
    

class Product(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/')
    product = models.FileField(upload_to='media/')
    price = models.PositiveIntegerField()
    
    def __str__(self):
        return (self.name)