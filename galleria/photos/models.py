from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=20)

class Location(models.Model):
    country = models.CharField(max_length=20)

class Images(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(upload_to ='images/', null=True,blank =False,width_field='width',height_field='height')
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name
