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
