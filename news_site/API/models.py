from django.db import models


class JsonInputDate(models.Model):
    name = models.CharField(max_length=49)
    date = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вводимая информация'
        verbose_name_plural = 'Вводимая информация'
        ordering = ['name', 'date']
