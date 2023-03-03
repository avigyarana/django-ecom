from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)
    primaryCategory = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Product(models.Model):
    mainimage = models.ImageField(upload_to='products/', blank=True)
    name = models.CharField(max_length=300)
    slug = models.SlugField()
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    preview_text = models.TextField(max_length=200, verbose_name='preview text')
    detail_text = models.TextField(max_length=500, verbose_name="detail text")
    price = models.FloatField()

    def __str__(self):
        return self.name

