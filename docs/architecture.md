# System Architecture - Taller Mecánico Management System

## Component Architecture

### 1. Django Application Structure
```
taller_mecanico/
├── taller_mecanico/        # Main project package
│   ├── __init__.py
│   ├── settings.py         # Configuration
│   ├── urls.py            # URL routing
│   ├── wsgi.py            # WSGI application
│   └── asgi.py            # ASGI application
├── trabajadores/          # Workers management app
│   ├── models.py          # Worker data model
│   ├── views.py           # CRUD views
│   ├── forms.py           # ModelForm
│   ├── urls.py            # App routing
│   └── tests.py           # Test suite
├── empresa/               # Company management app
│   ├── models.py          # Company data model
│   ├── views.py           # Single instance views
│   ├── forms.py           # ModelForm
│   ├── urls.py            # App routing
│   └── tests.py           # Test suite
├── productos/             # Product management app
│   ├── models.py          # Product data model
│   ├── views.py           # CRUD views
│   ├── forms.py           # ModelForm with IVA logic
│   ├── urls.py            # App routing
│   └── tests.py           # Test suite
├── proveedores/           # Supplier management app
│   ├── models.py          # Supplier data model
│   ├── views.py           # CRUD views
│   ├── forms.py           # ModelForm
│   ├── urls.py            # App routing
│   └── tests.py           # Test suite
├── templates/             # Shared templates
│   ├── base.html          # Base template
│   ├── home.html          # Static homepage
│   └── [app_templates]/   # App-specific templates
├── static/                # Static assets
│   ├── css/
│   ├── js/
│   └── images/
└── media/                 # User uploads
```

### 2. Interface Definitions and Contracts

#### Model Interface Contract
```python
class BaseModel(models.Model):
    """Base model interface for all entities"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
    
    def clean(self) -> None:
        """Validate model instance"""
        pass
    
    def __str__(self) -> str:
        """String representation"""
        pass
```

#### View Interface Contract
```python
class BaseCRUDView:
    """Interface contract for CRUD operations"""
    model = None
    form_class = None
    template_name = None
    success_url = None
    
    def get_queryset(self):
        """Return filtered queryset"""
        pass
    
    def get_context_data(self, **kwargs):
        """Add context for templates"""
        pass
    
    def form_valid(self, form):
        """Handle valid form submission"""
        pass
```

#### Form Interface Contract
```python
class BaseModelForm(forms.ModelForm):
    """Base form with common validation"""
    
    def clean(self):
        """Cross-field validation"""
        pass
    
    def save(self, commit=True):
        """Save with additional processing"""
        pass
```

### 3. Dependency Injection and Inversion of Control

#### Service Layer Pattern
```python
class EntityService:
    """Service layer for business logic"""
    
    def __init__(self, repository):
        self.repository = repository
    
    def create_entity(self, data):
        """Business logic for creation"""
        pass
    
    def update_entity(self, entity_id, data):
        """Business logic for updates"""
        pass
```

#### Repository Pattern
```python
class EntityRepository:
    """Data access layer"""
    
    def __init__(self, model_class):
        self.model = model_class
    
    def get_all(self):
        """Retrieve all entities"""
        return self.model.objects.all()
    
    def get_by_id(self, entity_id):
        """Retrieve by primary key"""
        return self.model.objects.get(pk=entity_id)
    
    def create(self, **kwargs):
        """Create new entity"""
        return self.model.objects.create(**kwargs)
```

### 4. Configuration Management Strategy

#### Environment-Based Settings
```python
# settings.py
import os
from pathlib import Path

# Environment variables for deployment
DEBUG = os.getenv('DJANGO_DEBUG', 'True').lower() == 'true'
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'default-dev-key')

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'practicatpe2'),
        'USER': os.getenv('DB_USER', 'practicausr25'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'practic35'),
        'HOST': os.getenv('DB_HOST', 'db'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

# Media and static files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

## Data Architecture

### 1. Database Schema Design

#### Entity Relationship Diagram
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Trabajadores  │    │     Empresa     │    │   Productos     │
├─────────────────┤    ├─────────────────┤    ├─────────────────┤
│ id (PK)         │    │ id (PK)         │    │ id (PK)         │
│ nombre          │    │ nombre          │    │ nombre          │
│ apellido        │    │ direccion       │    │ descripcion     │
│ correo (UNIQUE) │    │ mision          │    │ precio          │
│ cedula (UNIQUE) │    │ vision          │    │ iva (0 or 15)   │
│ codigo_empleado │    │ anio_fundacion  │    │ imagen          │
│ imagen          │    │ ruc (UNIQUE)    │    │ created_at      │
│ created_at      │    │ imagen          │    │ updated_at      │
│ updated_at      │    │ created_at      │    └─────────────────┘
└─────────────────┘    │ updated_at      │    
                       └─────────────────┘    ┌─────────────────┐
                                              │  Proveedores    │
                                              ├─────────────────┤
                                              │ id (PK)         │
                                              │ nombre          │
                                              │ descripcion     │
                                              │ telefono        │
                                              │ pais            │
                                              │ correo          │
                                              │ direccion       │
                                              │ created_at      │
                                              │ updated_at      │
                                              └─────────────────┘
```

#### Database Constraints and Indexes
```sql
-- Trabajadores table
CREATE INDEX idx_trabajadores_codigo_empleado ON trabajadores(codigo_empleado);
CREATE UNIQUE INDEX idx_trabajadores_cedula ON trabajadores(cedula);
CREATE UNIQUE INDEX idx_trabajadores_correo ON trabajadores(correo);

-- Empresa table (single instance constraint)
CREATE UNIQUE INDEX idx_empresa_singleton ON empresa((TRUE));

-- Productos table
CREATE INDEX idx_productos_precio ON productos(precio);
CREATE INDEX idx_productos_iva ON productos(iva);

-- Proveedores table
CREATE INDEX idx_proveedores_pais ON proveedores(pais);
CREATE INDEX idx_proveedores_correo ON proveedores(correo);
```

### 2. Data Access Patterns and Repositories

#### QuerySet Optimization
```python
class OptimizedQuerysets:
    @staticmethod
    def get_all_trabajadores():
        """Optimized query for workers list"""
        return Trabajador.objects.select_related().order_by('apellido', 'nombre')
    
    @staticmethod
    def get_productos_with_pricing():
        """Products with calculated pricing"""
        return Producto.objects.annotate(
            precio_con_iva=Case(
                When(iva=15, then=F('precio') * 1.15),
                default=F('precio'),
                output_field=DecimalField(max_digits=10, decimal_places=2)
            )
        )
```

### 3. Caching Strategies and Data Flow

#### Multi-Level Caching
```python
# Template fragment caching
{% load cache %}
{% cache 300 company_info %}
    {{ company.nombre }} - {{ company.direccion }}
{% endcache %}

# Database query caching
from django.core.cache import cache

def get_empresa_info():
    empresa = cache.get('empresa_instance')
    if empresa is None:
        empresa = Empresa.objects.first()
        cache.set('empresa_instance', empresa, 3600)  # 1 hour
    return empresa
```

### 4. Backup and Recovery Procedures

#### Database Backup Strategy
```bash
# Docker-based backup
docker-compose exec db pg_dump -U practicausr25 practicatpe2 > backup_$(date +%Y%m%d_%H%M%S).sql

# Automated backup script
#!/bin/bash
BACKUP_DIR="/backups"
DATE=$(date +%Y%m%d_%H%M%S)
docker-compose exec -T db pg_dump -U practicausr25 practicatpe2 | gzip > $BACKUP_DIR/backup_$DATE.sql.gz

# Keep last 7 days of backups
find $BACKUP_DIR -name "backup_*.sql.gz" -mtime +7 -delete
```

## Infrastructure Architecture

### 1. Deployment Architecture and Environments

#### Development Environment (Docker Compose)
```yaml
# docker-compose.yml
services:
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: practicatpe2
      POSTGRES_USER: practicausr25
      POSTGRES_PASSWORD: practic35
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U practicausr25 -d practicatpe2"]
      interval: 30s
      timeout: 10s
      retries: 3

  web:
    build: .
    volumes:
      - .:/app
      - ./media:/app/media
    ports:
      - "8000:8000"
    depends_on:
      db:
        condition: service_healthy
    environment:
      - DJANGO_SETTINGS_MODULE=taller_mecanico.settings
```

#### Production Environment Architecture
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Load Balancer │    │   Web Server    │    │   Database      │
│   (nginx)       │────│   (Gunicorn)    │────│   (PostgreSQL)  │
│   Port 80/443   │    │   Port 8000     │    │   Port 5432     │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │              ┌─────────────────┐              │
         │              │   Static Files  │              │
         └──────────────│   (nginx)       │──────────────┘
                        │   /static/      │
                        │   /media/       │
                        └─────────────────┘
```

### 2. CI/CD Pipeline Design

#### GitHub Actions Workflow
```yaml
# .github/workflows/ci-cd.yml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_PASSWORD: postgres
          POSTGRES_DB: test_db
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python 3.13
      uses: actions/setup-python@v4
      with:
        python-version: 3.13
    
    - name: Install UV
      run: pip install uv
    
    - name: Install dependencies
      run: uv sync
    
    - name: Run tests
      run: uv run coverage run -m pytest
    
    - name: Check coverage
      run: uv run coverage report --fail-under=80
```

### 3. Monitoring and Logging Architecture

#### Application Monitoring
```python
# settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'django.log',
            'formatter': 'verbose',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': 'INFO',
    },
}
```

### 4. Security Architecture and Access Controls

#### Security Configuration
```python
# Security settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_SECONDS = 31536000 if not DEBUG else 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# File upload security
FILE_UPLOAD_MAX_MEMORY_SIZE = 5242880  # 5MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 5242880
ALLOWED_IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif']

# CSRF protection
CSRF_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_HTTPONLY = True
```

#### Input Validation Layer
```python
class SecurityValidator:
    @staticmethod
    def validate_image_file(file):
        """Validate uploaded image files"""
        if not file.content_type.startswith('image/'):
            raise ValidationError('File must be an image')
        
        if file.size > 5 * 1024 * 1024:  # 5MB limit
            raise ValidationError('Image file too large')
        
        # Additional security checks
        try:
            Image.open(file).verify()
        except Exception:
            raise ValidationError('Invalid image file')
```

## Performance Optimization

### Database Query Optimization
- Use `select_related()` for forward relationships
- Use `prefetch_related()` for reverse relationships
- Implement database-level constraints and indexes
- Use `annotate()` for calculated fields

### Caching Strategy
- Template fragment caching for static content
- Database query result caching
- Static file caching with proper headers
- Browser caching optimization

### Memory Management
- Use `@dataclass(slots=True)` for data structures
- Implement lazy loading for images
- Optimize QuerySet evaluation timing
- Monitor memory usage with profiling tools

Target: Sub-200ms response times for all CRUD operations with 80% test coverage