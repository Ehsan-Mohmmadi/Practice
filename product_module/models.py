from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام محصول')
    price = models.FloatField(verbose_name='قیمت')
    in_stock = models.BooleanField(verbose_name='موجود')
    
    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self):
        return self.name
