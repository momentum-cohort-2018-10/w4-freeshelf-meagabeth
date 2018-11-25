from django.db import models
from django.template.defaultfilters import slugify
from datetime import date


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    date_added = date.today()
    url = models.URLField()
    image = models.ImageField(upload_to='books/', null=True)

    def save(self):
        if not self.id: 
            self.slug = slugify(self.title)
        super(Book, self).save()

