from django.db import models
from django.template.defaultfilters import slugify
from datetime import datetime
# from PIL import Image


# Create your models here.
# class Date_Added(models.Model):
#     added = models.DateTimeField(auto_now_add=True)
# BOOK_CATEGORY_CHOICES = (
#     ('african', 'African'),
#     ('medival', 'Medival'),
#     ('20th century', '20th Century'),
#     ('american', 'American'),
#     ('european', 'European'),
# )

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    # date_added = date.today()
    # category = models.CharField(max_length=255)
    url = models.URLField()
    # image = models.ImageField(upload_to='books/', null=True)
    african_art = models.BooleanField(default=False)
    american_art = models.BooleanField(default=False)
    medival_art = models.BooleanField(default=False)
    european_art = models.BooleanField(default=False)
    twentieth_cent_art = models.BooleanField(default=False)

    def save(self):
        if not self.id:
            self.slug = slugify(self.title)
        super(Book, self).save()

    def categories(self):
        categories = []
        if self.african_art:
            categories.append("African Art")
        if self.american_art:
            categories.append("American Art")
        if self.medival_art:
            categories.append("Medival Art")
        if self.european_art:
            categories.append("European Art")
        if self.twentieth_cent_art:
            categories.append("20th Century Art")
        return categories


    def __str__(self):
        return self.title


# class Category(models.Model):
#     name = models.TextField(max_length=50)
#     slug = models.SlugField(unique=True)

#     def __str__(self):
#         return self.name
