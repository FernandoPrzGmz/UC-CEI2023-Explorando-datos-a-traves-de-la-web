# Generated by Django 3.2.22 on 2023-11-09 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(blank=True, max_length=30, null=True, verbose_name='Tipo de producto')),
                ('status', models.CharField(max_length=30, verbose_name='Estado del viaje')),
                ('request_time', models.DateTimeField(verbose_name='Fecha y hora de la solicitud')),
                ('begin_time', models.DateTimeField(blank=True, null=True, verbose_name='Fecha y hora del inicio del viaje')),
                ('begin_latitude', models.FloatField(blank=True, null=True, verbose_name='Latitud del inicio del viaje')),
                ('begin_longitude', models.FloatField(blank=True, null=True, verbose_name='Longitud del inicio del viaje')),
                ('dropoff_time', models.DateTimeField(blank=True, null=True, verbose_name='Fecha y hora del fin del viaje')),
                ('dropoff_latitude', models.FloatField(blank=True, null=True, verbose_name='Latitud del fin del viaje')),
                ('dropoff_longitude', models.FloatField(blank=True, null=True, verbose_name='Longitud del fin del viaje')),
                ('distance', models.FloatField(help_text='Expresado en millas', verbose_name='Distancia')),
                ('fare_amount', models.FloatField(verbose_name='Monto de la tarifa')),
                ('fare_currency', models.CharField(blank=True, max_length=10, null=True, verbose_name='Tarifa de la divisa')),
            ],
            options={
                'verbose_name': 'Viaje',
                'verbose_name_plural': 'Viajes',
            },
        ),
    ]