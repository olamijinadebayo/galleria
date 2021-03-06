from django.db import models

# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.category

    def save_category(self):
        self.save()

    def delete_category(self):
        '''
        Method to delete a category from the database
        '''
        self.delete()

    @classmethod
    def update_cat(cls, id, new_category):
        cls.objects.filter(id=id).update(category=new_category)


class Location(models.Model):
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.country

    def save_location(self):
        self.save()

    @classmethod
    def update_location(cls, id, new_country):
        cls.objects.filter(id=id).update(country=new_country)

    def delete_location(self):
        '''
        Method to delete a location from the database
        '''
        self.delete()


class Images(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=40)
    image = models.ImageField(upload_to='images/', null=True, blank=False)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name

    def save_images(self):
        self.save()

    def delete_images(self):
        '''
        Method to delete a images from the database
        '''
        self.delete()

    class Meta:
        ordering = ['category']

    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image

    @classmethod
    def search_by_category(cls, search_term):
        category = cls.objects.filter(category__category__icontains=search_term)
        return category

    @classmethod
    def kenyan_images(cls):
        kenyan_photos = cls.objects.filter(location__country='Kenya')
        return kenyan_photos

    @classmethod
    def nigerian_images(cls):
        nigerian_photos = cls.objects.filter(location__country='Nigeria')
        return nigerian_photos
