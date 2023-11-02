from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='news/images/', null=True, blank=True, verbose_name="фото")
    video = models.FileField(upload_to='news/videos/', null=True, blank=True, verbose_name="Видео")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = "Продукт"
