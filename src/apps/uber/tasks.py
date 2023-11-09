import time
from celery import shared_task
from datetime import datetime

from src.apps.uber.utils import get_dataframe

@shared_task
def add(x, y, delay=0):
    time.sleep(delay)
    return x + y


@shared_task
def mul(x, y, delay=0):
    time.sleep(delay)
    return x * y



@shared_task
def total_trips_per_year():
    """
    Obtiene el total de viajes por año
    """
    rides_df = get_dataframe()
    rides_df['year'] = rides_df['request_time'].map(lambda request_time: datetime.strftime(request_time,"%Y"))
    df = rides_df['year'].value_counts().sort_index(ascending=True)
    return(df.to_json())


@shared_task
def percentage_trips_per_status_and_year():
    """
    Obtiene el porcentaje de viajes por estado y por año
    """
    rides_df = get_dataframe()
    rides_df['year'] = rides_df['request_time'].map(lambda request_time: datetime.strftime(request_time,"%Y"))
    # df = rides_df.groupby(by=['year'])['status'].value_counts(normalize=True)
    # return(df.to_json())

    # Agrupa los datos por 'year' y 'status', calcula las frecuencias normalizadas
    grouped_df = rides_df.groupby(by=['year', 'status']).size().reset_index(name='count')
    grouped_df['normalized_count'] = grouped_df.groupby('year')['count'].transform(lambda x: x / x.sum())

    # Pivotea la tabla para obtener las columnas deseadas
    pivot_df = grouped_df.pivot(index='year', columns='status', values='normalized_count').reset_index()

    # Rellena los valores NaN con 0
    pivot_df = pivot_df.fillna(0)

    # Cambia los nombres de las columnas
    pivot_df.columns.name = None

    # Reordena las columnas según tu solicitud
    pivot_df = pivot_df[['year', 'COMPLETED', 'CANCELED', 'DRIVER_CANCELED', 'UNFULFILLED']]

    # Muestra el DataFrame final
    return pivot_df.to_json()
