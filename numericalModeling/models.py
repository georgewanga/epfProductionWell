from django.db import models


class NumericalModelingTable(models.Model):
    Date = models.CharField(max_length=50)
    Flow_Rate = models.CharField(max_length=50)
    Totals = models.CharField(max_length=50)

    objects = models.Manager()  # The default manager

    def __str__(self):
        return self.Date

    class Meta:
        verbose_name_plural = "NumericalModelingTable"

