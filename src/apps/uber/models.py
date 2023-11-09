from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Trip(models.Model):
    product_type = models.CharField(
        verbose_name='Tipo de producto', 
        max_length=30,
        null=True,
        blank=True,
    )
    status = models.CharField(
        verbose_name='Estado del viaje', 
        max_length=30,
    )
    request_time = models.DateTimeField(
        verbose_name='Fecha y hora de la solicitud',
    )
    
    begin_time = models.DateTimeField(
        verbose_name='Fecha y hora del inicio del viaje',
        null=True,
        blank=True,
    )
    begin_latitude = models.FloatField(
        verbose_name='Latitud del inicio del viaje',
        null=True,
        blank=True,
    )
    begin_longitude = models.FloatField(
        verbose_name='Longitud del inicio del viaje',
        null=True,
        blank=True,
    )
    
    dropoff_time = models.DateTimeField(
        verbose_name='Fecha y hora del fin del viaje',
        null=True,
        blank=True,
    )
    dropoff_latitude = models.FloatField(
        verbose_name='Latitud del fin del viaje',
        null=True,
        blank=True,
    )
    dropoff_longitude = models.FloatField(
        verbose_name='Longitud del fin del viaje',
        null=True,
        blank=True,
    )

    distance = models.FloatField(
        verbose_name='Distancia',
        help_text='Expresado en millas',
    )
    fare_amount = models.FloatField(
        verbose_name='Monto de la tarifa',
    )
    fare_currency = models.CharField(
        verbose_name='Tarifa de la divisa',
        max_length=10,
        null=True,
        blank=True,
    )
    class Meta:
        verbose_name = 'Viaje'
        verbose_name_plural = 'Viajes'

    def __str__(self):
        return F"{self.product_type} - {self.status}"
    