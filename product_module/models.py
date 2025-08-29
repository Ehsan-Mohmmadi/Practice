from tkinter.constants import CASCADE

from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name='نام دسته بندی')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام محصول')
    price = models.FloatField(verbose_name='قیمت')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='دسته بندی')
    slug = models.SlugField()
    in_stock = models.BooleanField(verbose_name='موجود')

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)