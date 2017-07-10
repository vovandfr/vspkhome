from django.db import models


class Address(models.Model):
    address = models.CharField(max_length=400, null=True, blank=True)

    class Meta():
        verbose_name = 'Адрес субъекта'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return self.address
