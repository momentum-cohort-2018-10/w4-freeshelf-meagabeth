from django.db import models
from django.template.defaultfilters import slugify
from datetime import datetime
# from PIL import Image


# Create your models here.
# class Date_Added(models.Model):
#     added = models.DateTimeField(auto_now_add=True)


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    # date_added = date.today()
    # category = models.CharField(max_length=255)
    url = models.URLField()
    # image = models.ImageField(upload_to='books/', null=True)

    def save(self):
        if not self.id:
            self.slug = slugify(self.title)
        super(Book, self).save()

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.TextField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
