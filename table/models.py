from django.db import models


# Create your models here.
class TableModel(models.Model):

    name = models.CharField('name', max_length=120)
    result = models.CharField('result', max_length=120)

    class Meta:
        verbose_name = 'Table'

    def __str__(self):
        return self.name
