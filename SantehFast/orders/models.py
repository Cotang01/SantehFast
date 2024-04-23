from django.db import models


class Order(models.Model):
    phone = models.CharField(max_length=15, blank=False, null=False)
    full_name = models.CharField(max_length=30, blank=True, null=True)
    repair_category = models.CharField(max_length=20, blank=False, null=False)
    address = models.CharField(max_length=100, blank=False, null=False)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'Заказчик: {self.phone} {self.full_name} ' \
               f'Тема: {self.repair_category} ' \
               f'Статус выполнения: {self.status}'

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'
