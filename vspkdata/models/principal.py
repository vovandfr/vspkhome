from django.db import models
from vspkdata.models import GlobalCode
from vspkdata.models import Entity


class Principal(models.Model):
    code = models.ForeignKey(GlobalCode, on_delete=models.CASCADE, null=True)
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, null=True)
    position = models.CharField(max_length=200)
    appointment = models.DateField(auto_now=False,
                                   auto_now_add=False,
                                   null=True,
                                   blank=True)

    class Meta():
        verbose_name = 'Руководитель'
        verbose_name_plural = 'Руководители'
        ordering = ['entity', 'appointment', ]

    def __str__(self):
        separator = " - "
        text = (str(self.entity.code),
                self.position,
                str(self.code),
                str(self.appointment))
        return separator.join(text)
