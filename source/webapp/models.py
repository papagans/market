from django.db import models
category = (
    ('other', 'Разное'),
    ('processors', 'Процессоры'),
    ('monitors', 'Мониторы'),
    ('hdd', 'Жесткие диски'),
    ('ddr', 'Оперативная память')
)


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Наименование товара')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание товара')
    category = models.CharField(max_length=20, default=category[0][0], verbose_name='Status', choices=category)
    count = models.PositiveIntegerField(verbose_name='Остаток')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.name
# Create your models here.
