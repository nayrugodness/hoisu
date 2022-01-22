from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.shortcuts import reverse

class UserHoisu(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

category = [
    [0, "Restaurant"],
    [1, "Coffee Shop"],
    [2, "Bar"]
]


states = [
    [0, "Open"],
    [1, "Close"]
]
class City(models.Model):
    code = models.CharField(max_length=50)
    city = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.code} -> {self.city}'

class Establishment(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='media')
    size = models.PositiveIntegerField(default=0)
    state = models.IntegerField(choices=states)
    country = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    category = models.IntegerField(choices=category)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("establishment:establisment-info", kwargs={'slug': self.slug})


type_query = [
    [0, "Query"],
    [1, "Claim"],
    [2, "Suggestion"],
    [3, "Praise"]
]
