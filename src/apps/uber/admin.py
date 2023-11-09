from django.contrib import admin
from src.apps.uber.models import Trip

# Register your models here.
@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'product_type', 
        'status', 
        'request_time', 
        'begin_time', 
        'begin_latitude', 
        'begin_longitude', 
        'dropoff_time', 
        'dropoff_latitude', 
        'dropoff_longitude', 
        'distance', 
        'fare_amount', 
        'fare_currency', 
    )
