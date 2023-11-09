# UC-CEI2023 Explorando datos a través de la web: Introducción a Django para la ingeniería en datos

## Descripción

Este proyecto forma parte de los recursos desarrollados para el taller: "Explorando datos a través de la web: Introducción a Django para la ingeniería en datos" del Congreso de Estudiantes de Ingenierías 2023 de la Universidad del Caribe.


## Instrucciones de uso

1. Construir la imagen de docker.

```bash
sudo docker build --no-cache -t cei2023-django .
```

2. Iniciar el contenedor con la imagen.

Exponemos el puerto 8000 y bindeamos la carpeta donde estamos posicionados.

```bash
sudo docker run \
    --name cei2023-django \
    -p 8000:8000 \
    -p 6655:6655 \
    -v $(pwd):/app/cei2023-django \
    -v $(pwd)/test:/app/hello-world \
    -d cei2023-django
```

3. Entrar al contenedor

```bash
sudo docker exec -it cei2023-django /bin/bash
```

4. Reiniciar el servicio de redis-server

```bash
service redis-server restart

# Podemos comprobar que redis funciona con lo siguiente
redis-cli ping
```

5. Iniciar el worker y flower
```
cd /app/cei2023-django/
celery -A src flower --port=6655 --auto_refresh=True
```

```
cd /app/cei2023-django/
celery -A src worker
```

6. Cargar los datos datos iniciales de nuestra base de datos
```bash
python manage.py loaddata src/.db_fixtures/dumpdata.json
```