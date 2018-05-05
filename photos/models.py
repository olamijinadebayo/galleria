from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=20)
    def __str__(self):
        return self.category
class Location(models.Model):
    country = models.CharField(max_length=20)
    def __str__(self):
        return self.country
class Images(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=40)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(upload_to ='images/', null=True,blank =False,width_field='width',height_field='height')
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['category']
    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def search_by_category(cls,search_term):
        category = cls.objects.filter(category__category__icontains=search_term)
        return category
