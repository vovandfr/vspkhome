from django.db import models
from vspkdata.models import GlobalCode
from vspkdata.models import Address
from vspkdata.models import Activity


class Entity(models.Model):
    code = models.ForeignKey(GlobalCode, on_delete=models.CASCADE, null=True)
    full_name = models.CharField(max_length=400)
    short_name = models.CharField(max_length=200, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    share_capital = models.DecimalField(max_digits=17,
                                        decimal_places=2,
                                        default=0)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, null=True)
    date_of_registration = models.DateField(auto_now=False, auto_now_add=False)
    correction = models.DateField(auto_now=False, auto_now_add=False)

    class Meta():
        verbose_name = 'Предприятие'
        verbose_name_plural = 'Предприятия'
        ordering = ['code', ]

    def __str__(self):
        separator = " - "
        text = (str(self.code), self.full_name)
        return separator.join(text)
