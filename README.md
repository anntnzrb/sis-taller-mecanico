# Sistema de Taller Mecánico

Aplicación web Django para gestión de taller mecánico con CRUD para trabajadores, empresa, productos y proveedores.

## Ejecutar

### Con Docker
```bash
docker-compose up --build
```

### Sin Docker
```bash
uv sync

# PostgreSQL
sudo -u postgres psql
CREATE DATABASE practicatpe2;
CREATE USER practicausr25 WITH PASSWORD 'practic35';
GRANT ALL PRIVILEGES ON DATABASE practicatpe2 TO practicausr25;
\q

# Ejecutar
uv run python manage.py migrate
uv run python manage.py runserver
```

**Ver**: http://localhost:8000

## Tests
```bash
docker-compose exec web uv run python manage.py test
```

## Producción
```bash
# Variables de entorno
export SECRET_KEY=tu-clave-secreta-segura
export DEBUG=False
export ALLOWED_HOSTS=tudominio.com

# Despliegue
pip install gunicorn
python manage.py migrate
python manage.py collectstatic
gunicorn taller_mecanico.wsgi:application --bind 0.0.0.0:8000
```