from django.db import models


class MercuryManometerTable(models.Model):
    Time = models.CharField(max_length=50)
    Differential_Pressure = models.CharField(max_length=50)
    Weir_Height = models.CharField(max_length=50)
    Upstream_Pressure = models.CharField(max_length=50)
    Steam_flow_rate = models.CharField(max_length=50)
    Corr_Water_flow = models.CharField(max_length=50)
    Mass_Flow_rate = models.CharField(max_length=50)
    Stream_enthalpy = models.CharField(max_length=50)
    combined_enthalpy = models.CharField(max_length=50)
    Whp = models.CharField(max_length=50)

    objects = models.Manager()  # The default manager

    # To avoid saving every entry as MercuryManometerTable object and use the Time as default name
    def __str__(self):
        return self.Time

    # saving as MercuryManometerTable not MercuryManometerTables
    class Meta:
        verbose_name_plural = "MercuryManometerTable"
