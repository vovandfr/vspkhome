from django.db import models


class Activity(models.Model):
    code = models.CharField(max_length=10, null=False, blank=False)
    activity = models.CharField(max_length=400, null=True, blank=True)

    class Meta():
        verbose_name = 'Вид деятельности'
        verbose_name_plural = 'Виды деятельности'
        ordering = ['code', ]

    def __str__(self):
        separator = " - "
        text = (self.code, self.activity)
        return separator.join(text)
