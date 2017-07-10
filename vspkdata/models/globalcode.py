from django.db import models


class GlobalCode(models.Model):
    globalcode = models.BigIntegerField(primary_key=True)

    class Meta():
        verbose_name = 'Код субъекта'
        verbose_name_plural = 'Коды'
        ordering = ['globalcode', ]

    def __str__(self):
        code = str(self.globalcode)
        return code
