# Sistema de Taller Mecánico

Aplicación web Django para gestión de taller mecánico con CRUD completo.

## Ejecutar

```bash
docker-compose up --build -d
docker-compose exec web uv run python manage.py migrate
```

**Ver**: http://localhost:8000

## Tests

```bash
docker-compose exec web uv run python manage.py test
```
