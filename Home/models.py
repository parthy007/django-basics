from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.EmailField(max_length=254)
    name = models.CharField(max_length=122)
    address = models.CharField(max_length=12)
    city = models.CharField(max_length=122)
    zip = models.IntegerField()