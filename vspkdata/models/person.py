from django.db import models
from vspkdata.models import GlobalCode
from vspkdata.models import Address


class Person(models.Model):
    code = models.ForeignKey(GlobalCode, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)

    class Meta():
        verbose_name = 'Физлицо'
        verbose_name_plural = 'Физлица'
        ordering = ['last_name', 'code', ]

    def __str__(self):
        code = str(self.code)
        dob = str(self.date_of_birth)
        text = code
        text += " - " + self.last_name
        text += " " + self.first_name
        if (self.middle_name):
            text += " " + self.middle_name
        text += ", " + dob
        return text
