from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='Category Name')
    details = models.CharField(max_length=500, verbose_name='Category Details')