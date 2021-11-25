from django.core import validators
from django.db import models
from django.core.validators import MaxValueValidator

class Category(models.Model):
    name = models.CharField(max_length=250)
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to = 'upload/')
    rating = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5)])
    price = models.PositiveIntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    stock = models.ForeignKey('Stock', on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.name

class Stock(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.title
    


