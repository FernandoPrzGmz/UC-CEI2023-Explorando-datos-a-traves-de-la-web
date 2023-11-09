import pandas as pd
import datetime
from src.apps.uber.models import Trip


def get_dataframe():
    # Filtro por rango de fecha para remover datos incompletos del 2015 y del 2021
    queryset = Trip.objects.filter(request_time__range=[datetime.date(2016, 1, 1), 
                                                        datetime.date(2021, 1, 1)])
    return pd.DataFrame(list(queryset.values()))
