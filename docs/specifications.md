# Technical Specifications - Taller Mecánico Management System

## Project Overview
Django 5.2.2 web application for mechanical workshop management with complete CRUD operations across 4 core business entities.

## Functional Requirements

### Core Entities & Data Models
1. **Trabajadores (Workers)**
   - Fields: nombre, apellido, correo, cedula, codigo_empleado, imagen
   - UI: Horizontal cards layout (2 columns)
   - Section: "NUESTRO PERSONAL"

2. **Empresa (Company)**
   - Fields: nombre, direccion, mision, vision, anio_fundacion, ruc, imagen
   - UI: Single instance with conditional display logic
   - Section: "NOSOTROS" with dynamic content

3. **Productos (Products)**
   - Fields: nombre, descripcion, precio, iva (15 or 0), imagen
   - UI: Vertical cards grid (3 columns)
   - Section: "NUESTROS PRODUCTOS"

4. **Proveedores (Suppliers)**
   - Fields: nombre, descripcion, telefono, pais, correo, direccion
   - UI: Vertical cards grid (3 columns)
   - Section: "NUESTROS PROVEEDORES"

### API Endpoints (RESTful)
```
GET  /                          # Home page (static)
GET  /nosotros/                 # Company info
POST /nosotros/create/          # Create company
GET  /nosotros/edit/           # Edit company
POST /nosotros/update/         # Update company

GET  /trabajadores/            # List workers
GET  /trabajadores/create/     # Create worker form
POST /trabajadores/create/     # Create worker
GET  /trabajadores/<id>/edit/  # Edit worker form
POST /trabajadores/<id>/edit/  # Update worker
POST /trabajadores/<id>/delete/ # Delete worker

GET  /productos/               # List products
GET  /productos/create/        # Create product form
POST /productos/create/        # Create product
GET  /productos/<id>/edit/     # Edit product form
POST /productos/<id>/edit/     # Update product
POST /productos/<id>/delete/   # Delete product

GET  /proveedores/             # List suppliers
GET  /proveedores/create/      # Create supplier form
POST /proveedores/create/      # Create supplier
GET  /proveedores/<id>/edit/   # Edit supplier form
POST /proveedores/<id>/edit/   # Update supplier
POST /proveedores/<id>/delete/ # Delete supplier
```

## Non-Functional Requirements

### Performance
- Database query optimization with select_related/prefetch_related
- Image optimization and lazy loading
- PostgreSQL indexing for frequently queried fields

### Security
- Django's built-in CSRF protection
- Input validation through ModelForms
- XSS protection with template escaping
- File upload security for images

### Scalability
- Docker containerization
- PostgreSQL connection pooling
- Static file serving optimization

### Code Quality
- 80% test coverage target
- Python 3.13 modern patterns
- Ruff linting and formatting
- Type hints on all functions

## Technical Architecture

### Technology Stack
- **Backend**: Python 3.13 + Django 5.2.2
- **Database**: PostgreSQL with psycopg2
- **Package Manager**: UV
- **Frontend**: HTML5, Bootstrap CSS, Vanilla JavaScript
- **Development**: Docker + Docker Compose
- **Testing**: Django TestCase with TDD approach

### Database Configuration
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'practicatpe2',
        'USER': 'practicausr25',
        'PASSWORD': 'practic35',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Project Structure
```
taller_mecanico/
├── taller_mecanico/         # Main project
├── trabajadores/           # Workers app
├── empresa/               # Company app
├── productos/             # Products app
├── proveedores/          # Suppliers app
├── static/               # CSS, JS, images
├── templates/            # HTML templates
├── media/                # User uploads
└── tests/                # Test modules
```

## Implementation Constraints

### Development Environment
- **MANDATORY**: Docker for all development
- **NO** local dependency installation
- All commands via: `docker-compose exec <container> <cmd>`

### Access Control
- **NO** authentication system
- **NO** user roles or permissions
- Complete public access to all CRUD operations
- Single-user application model

### UI/UX Constraints
- Bootstrap-based responsive design
- Mechanical workshop aesthetic (industrial colors)
- Image handling with placeholder fallbacks
- Specific layout patterns per entity type

## Success Criteria
- ✅ All CRUD operations functional
- ✅ PostgreSQL integration working
- ✅ 80% test coverage achieved
- ✅ Docker containerization complete
- ✅ Responsive UI with proper navigation
- ✅ Image upload/display working
- ✅ Code quality standards met