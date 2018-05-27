from django.test import TestCase
from .models import Images, Location, Category


class ImageTestClass(TestCase):
    def setUp(self):
        self.location = Location(country='Malindi')
        self.location.save()

        self.category = Category(category='Travel')
        self.category.save()

        self.image_test = Images(image='blotch/test.png', description='this is a test instance',
                                 location=self.location, category=self.category)
        self.image_test.save_images()

        self.image_test1 = Images(image='blotch/test.png', description='this is a test instance',
                                  location=self.location, category=self.category)
        self.image_test1.save_images()

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Images))

    def tearDown(self):
        Images.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

    def test_save_image(self):
        self.image_test.save_images()
        images = Images.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.image_test.save_images()
        self.image_test.delete_images()
        self.image_test1.delete_images()
        images = Images.objects.all()
        self.assertTrue(len(images) == 0)

    def test_get_image_by_id(self):
        found_img = self.image_test.get_image_by_id(self.image_test.id)
        img = Images.objects.filter(id=self.image_test.id)
        self.assertTrue(found_img, img)

    def tearDown(self):
        Images.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()


class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(country='Malindi')
        self.location.save()

    def tearDown(self):
        Location.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        Location.objects.all().delete()
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_update_location(self):
        new_location_name = 'Ukunda'
        self.location.update_location(self.location.id, new_location_name)
        changed_location = Location.objects.filter(country='Ukunda')
        self.assertTrue(len(changed_location) > 0)

    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)

    def tearDown(self):
        Location.objects.all().delete()


class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(category='Travel')
        self.category.save()

    def tearDown(self):
        Category.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        Category.objects.all().delete()
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)
