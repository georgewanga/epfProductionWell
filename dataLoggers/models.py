from django.db import models


class DataLoggersTable(models.Model):
    Date = models.CharField(max_length=50)
    Whp = models.CharField(max_length=50)
    Upstream = models.CharField(max_length=50)
    Downstream = models.CharField(max_length=50)
    Weir = models.CharField(max_length=50)

    objects = models.Manager()  # The default manager

    def __str__(self):
        return self.Date

    class Meta:
        verbose_name_plural = "DataLoggersTable"
