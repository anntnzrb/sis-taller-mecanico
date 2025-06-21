# Sistema de Taller Mecánico

Aplicación web Django completa para gestión de taller mecánico con operaciones CRUD para trabajadores, empresa, productos y proveedores.

## 🚀 Ejecutar

### Con Docker (Recomendado)
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

## ✨ Funcionalidades

- ✅ **CRUD Completo**: Trabajadores, Empresa, Productos, Proveedores
- ✅ **Interfaz Responsiva**: Bootstrap 5.3 con diseño móvil-primero  
- ✅ **Gestión de Imágenes**: Subida de fotos para trabajadores y empresa
- ✅ **Validaciones**: Formularios con validación personalizada
- ✅ **Base de Datos**: PostgreSQL con migraciones completas
- ✅ **Tests**: 89.5% cobertura con 39 tests comprehensivos
- ✅ **Idioma**: Interfaz completamente en español

## 🏗️ Arquitectura

```
├── trabajadores/     # Gestión de personal
├── empresa/         # Información de la empresa  
├── productos/       # Catálogo de productos
├── proveedores/     # Red de proveedores
├── templates/       # Plantillas HTML responsivas
├── static/         # CSS, JavaScript, imágenes
└── media/          # Archivos subidos por usuarios
```

## 🧪 Testing

```bash
# Ejecutar tests
docker-compose exec web uv run python manage.py test

# Ver cobertura
docker-compose exec web uv run coverage run --source='.' manage.py test
docker-compose exec web uv run coverage report
```

## 🚀 Producción

### Variables de Entorno
```bash
SECRET_KEY=tu-clave-secreta-segura
DEBUG=False
ALLOWED_HOSTS=tudominio.com
DATABASE_URL=postgresql://user:pass@host:port/dbname
```

### Despliegue
```bash
# Instalar dependencias
pip install gunicorn

# Migrar base de datos
python manage.py migrate

# Recopilar archivos estáticos
python manage.py collectstatic

# Ejecutar con gunicorn
gunicorn taller_mecanico.wsgi:application --bind 0.0.0.0:8000
```

### Configuración nginx
```nginx
server {
    listen 80;
    server_name tudominio.com;
    
    location /static/ {
        alias /ruta/a/staticfiles/;
    }
    
    location /media/ {
        alias /ruta/a/media/;
    }
    
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

## 🔒 Seguridad

- ✅ Protección CSRF habilitada
- ✅ Validación de entrada en todos los formularios
- ✅ Restricciones de subida de archivos
- ✅ Constraintes únicos en campos sensibles
- ✅ Protección contra inyección SQL (Django ORM)

## 📋 Checklist de Producción

- [ ] Configurar `SECRET_KEY` segura
- [ ] Establecer `ALLOWED_HOSTS`
- [ ] Configurar SSL/HTTPS
- [ ] Configurar servidor web (nginx/apache)
- [ ] Configurar base de datos de producción
- [ ] Configurar backup de base de datos
- [ ] Configurar monitoreo de errores

## 📖 Documentación

- **Especificaciones**: [docs/prd.md](docs/prd.md)
- **Guías de desarrollo**: [docs/python-guidelines.md](docs/python-guidelines.md)
- **Arquitectura**: [docs/architecture.md](docs/architecture.md)

---

**Stack**: Django 5.2.2 + PostgreSQL + Bootstrap 5.3  
**Cobertura de tests**: 89.5% (39 tests)  
**Metodología**: SPARC Automated Development System