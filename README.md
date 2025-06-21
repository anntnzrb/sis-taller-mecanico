# Sistema de Taller Mecánico

Aplicación web Django completa para gestión de taller mecánico con operaciones CRUD para trabajadores, empresa, productos y proveedores.

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

# Ejecutar (usar settings_local.py para localhost)
uv run python manage.py migrate ...
uv run python manage.py createsuperuser ...
uv run python manage.py runserver ...
```

**Ver**: http://localhost:8000

## Funcionalidades

- ✅ **CRUD Completo**: Trabajadores, Empresa, Productos, Proveedores
- ✅ **Interfaz Responsiva**: Bootstrap 5.3 con diseño móvil-primero  
- ✅ **Gestión de Imágenes**: Subida de fotos para trabajadores y empresa
- ✅ **Validaciones**: Formularios con validación personalizada
- ✅ **Base de Datos**: PostgreSQL con migraciones completas
- ✅ **Tests**: 89.5% cobertura con 39 tests comprehensivos
- ✅ **Idioma**: Interfaz completamente en español

## Arquitectura

```
├── trabajadores/     # Gestión de personal
├── empresa/         # Información de la empresa  
├── productos/       # Catálogo de productos
├── proveedores/     # Red de proveedores
├── templates/       # Plantillas HTML responsivas
├── static/         # CSS, JavaScript, imágenes
└── media/          # Archivos subidos por usuarios
```

## Producción

Para configuración de producción:
```bash
# Configurar variables de entorno
export DJANGO_SETTINGS_MODULE=taller_mecanico.settings_production
export SECRET_KEY="tu-clave-secreta-segura"
export ALLOWED_HOSTS="tu-dominio.com"

# Ejecutar con gunicorn
gunicorn taller_mecanico.wsgi:application
```

**Especificaciones**: [docs/prd.md](docs/prd.md)
**Guideliness**: [docs/python-guidelines.md](docs/python-guidelines.md)
