from django.db import models

# Create your models here.
class Exercise(models.Model):
    image = models.ImageField(upload_to='customer_images/', blank=True)
    title = models.CharField(max_length=20)
    desc = models.CharField(max_length=60)

    def __str__(self):
        return self.title
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    desc = models.TextField()

    def __str__(self):
        return self.name
#
