from django.db import models


class Category(models.Model):
    """Категория"""
    title = models.CharField(max_length=155, verbose_name="Название категории")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Products(models.Model):
    """Товары"""
    title = models.CharField(max_length=155,verbose_name='Название товара')
    image = models.ImageField(verbose_name="Изображение")
    price = models.DecimalField(max_digits=7, decimal_places=2, default=20.00)
    description = models.TextField(verbose_name="Описание товара")
    category = models.ForeignKey(to=Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='categories')
