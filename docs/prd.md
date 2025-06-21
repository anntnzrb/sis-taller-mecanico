---
tipo_tienda: "taller mecánico"
version: "1.0"
fecha: "2025"
---

# Aplicación Web Django - Documento de Requerimientos del Producto

## Descripción General del Proyecto
Desarrollar una aplicación web completa para un **{{ tipo_tienda }}** usando el framework Django con integración a base de datos PostgreSQL, implementando el patrón de diseño MVC (Modelo-Vista-Controlador) en Python con operaciones CRUD completas para múltiples entidades de negocio.

**IMPORTANTE: Este documento debe ser seguido estrictamente.**

## Stack Tecnológico
- **Python**: 3.13
- **Framework**: Django 5.2.2
- **Gestor de Paquetes**: UV (para manejo de dependencias y entornos virtuales)
- **Base de Datos**: PostgreSQL
- **Frontend**: HTML, CSS/Bootstrap, JavaScript
- **Adaptador de Base de Datos**: psycopg2

## Configuración de Base de Datos
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

## Estructura del Proyecto

### Configuración del Proyecto Django
1. Crear proyecto principal de Django
2. Configurar conexión a base de datos PostgreSQL
3. Crear cuatro aplicaciones Django:
   - `trabajadores` (Trabajadores)
   - `empresa` (Empresa)
   - `productos` (Productos)
   - `proveedores` (Proveedores)

### Modelos de Datos

#### Modelo Trabajador
```python
- nombre
- apellido
- correo
- cedula
- codigo_empleado
- imagen
```

#### Modelo Empresa
```python
- nombre
- direccion
- mision
- vision
- anio_fundacion
- ruc
- imagen
```

#### Modelo Producto
```python
- nombre
- descripcion
- precio
- iva (valores: 15 ó 0)
- imagen
```

#### Modelo Proveedor
```python
- nombre
- descripcion
- telefono
- pais
- correo
- direccion
```

## Requerimientos de la Aplicación

### Funcionalidad Principal
1. **Migración de Base de Datos**: Generar y aplicar migraciones para todos los modelos
2. **Operaciones CRUD**: Implementar funcionalidad completa de Crear, Leer, Actualizar, Eliminar para cada aplicación
3. **Vistas y Templates**: Crear vistas correspondientes y plantillas HTML para cada operación CRUD

### Estructura de Páginas y Navegación

**Estructura común en todas las páginas**:
- Título del sitio web + Logo del {{ tipo_tienda }} (parte superior)
- Menú de navegación estándar
- Contenido específico de cada página con estética apropiada para el {{ tipo_tienda }}

#### 1. Página Principal (Contenido Estático)
- **Ruta**: `/`
- **Contenido**: Información estática sobre el {{ tipo_tienda }} (NO depende de base de datos)
- **Implementación**: Directamente en HTML (sin datos dinámicos)
- **Estructura**:
  - Título del sitio web + Logo del {{ tipo_tienda }}
  - **Sección 1 - "DESCRIPCION DE LA EMPRESA"**: Carrusel de imágenes a la IZQUIERDA + Texto descriptivo a la DERECHA (4 imágenes relacionadas con el {{ tipo_tienda }})
  - **Sección 2 - "HISTORIA DE LA EMPRESA"**: Texto narrativo a la IZQUIERDA + Carrusel de imágenes a la DERECHA (4 imágenes sobre la historia del {{ tipo_tienda }})
  - Menú de navegación

**IMPORTANTE**: Esta página debe ser completamente estática, codificada directamente en HTML con contenido relacionado al {{ tipo_tienda }}.

#### 2. Página Nosotros (`/nosotros/`)
- **Lógica de navegación**:
  - **Cuando no existe información de empresa**: 
    - **Layout**: Tarjeta centrada con icono de advertencia
    - Mostrar "NO SE HA INGRESADO INFORMACION DE LA EMPRESA!!" 
    - Botón "AGREGAR INFORMACION" centrado → redirige a formulario de creación
  - **Cuando existe información de empresa**: 
    - **Layout**: 2 columnas con distribución específica
    - **Columna Izquierda**: Nombre de empresa, RUC, dirección, imagen (si existe), año de fundación
    - **Columna Derecha**: Botón "EDITAR INFORMACION" (esquina superior derecha), misión, visión
    - Botón "EDITAR INFORMACION" → redirige a formulario de edición
- **Nota**: Solo una empresa en el sistema (el {{ tipo_tienda }})

#### 3. Página Trabajadores (`/trabajadores/`)
- **Título de sección**: "NUESTRO PERSONAL"
- **Características**:
  - Mostrar todos los trabajadores del {{ tipo_tienda }} en formato de **tarjetas horizontales** (2 columnas)
  - **Layout de tarjeta**: Imagen del trabajador a la IZQUIERDA + Información a la DERECHA
  - **Botón "AGREGAR TRABAJADOR"**: Posicionado en la esquina superior derecha → redirige a formulario de creación
  - **Información mostrada**: Imagen del colaborador, nombre completo, correo, cédula, código de empleado
  - **Botones editar/eliminar**: Esquina superior derecha de cada tarjeta, completamente funcionales
  - **Estado sin trabajadores**: Componente de estado vacío centrado con opción para agregar primer trabajador

#### 4. Página Productos (`/productos/`)
- **Título de sección**: "NUESTROS PRODUCTOS"
- **Características**:
  - Mostrar todos los productos del {{ tipo_tienda }} en formato de grilla (3 columnas) con **tarjetas verticales**
  - **Layout de tarjeta**: Imagen del producto ARRIBA + Información ABAJO
  - **Botón "AGREGAR PRODUCTO"**: Posicionado en la esquina superior derecha → redirige a formulario de creación
  - **Información mostrada**: 
    - Imagen del producto (con placeholder de gradiente e ícono si no existe imagen)
    - Nombre del producto (centrado)
    - **Formato de precio**: Precio principal + "% IVA" en línea secundaria
  - **Botones editar/eliminar**: Parte inferior de cada tarjeta, completamente funcionales
  - **Estado sin productos**: Componente de estado vacío centrado con opción para agregar primer producto

#### 5. Página Proveedores (`/proveedores/`)
- **Título de sección**: "NUESTROS PROVEEDORES"
- **Características**:
  - Mostrar todos los proveedores del {{ tipo_tienda }} en formato de grilla (3 columnas) con **tarjetas verticales**
  - **Estructura de tarjeta**: Header con nombre del proveedor + Body con información detallada
  - **Botón "AGREGAR PROVEEDOR"**: Posicionado **centrado** en la parte superior → redirige a formulario de creación
  - **Información mostrada**: 
    - Header: Nombre del proveedor
    - Body: Correo, teléfono, país (cada campo con etiqueta y formato estructurado)
  - **Botones editar/eliminar**: Parte inferior de cada tarjeta, completamente funcionales
  - **Estado sin proveedores**: Componente de estado vacío centrado con opción para agregar primer proveedor

### Funcionalidad de Botones CRUD (Requisito Crítico)

**TODOS los botones deben ser completamente funcionales**:

1. **Botones de Creación**:
   - "AGREGAR TRABAJADOR" → formulario de creación de trabajador
   - "AGREGAR PRODUCTO" → formulario de creación de producto  
   - "AGREGAR PROVEEDOR" → formulario de creación de proveedor
   - "AGREGAR INFORMACION" (empresa) → formulario de creación de empresa

2. **Botones de Edición**:
   - Íconos de editar en cada tarjeta → formularios de edición correspondientes
   - "EDITAR INFORMACION" (empresa) → formulario de edición de empresa

3. **Botones de Eliminación**:
   - Íconos de eliminar en cada tarjeta → confirmación y eliminación del registro

**Todos los formularios deben coincidir exactamente con los campos especificados en cada modelo.**

### Menú de Navegación
Navegación estándar en todas las páginas (según diseños oficiales):
`HOME | NOSOTROS | PRODUCTOS | TRABAJADORES | PROVEEDORES`

## Requerimientos de Implementación Técnica

### 1. Configuración de URLs
- Configurar enrutamiento de URLs apropiado para todas las aplicaciones
- **URLs específicas para cada operación CRUD por aplicación**:
  - URLs para trabajadores (listar, crear, editar, eliminar)
  - URLs para empresa (listar, crear, editar, eliminar) 
  - URLs para productos (listar, crear, editar, eliminar)
  - URLs para proveedores (listar, crear, editar, eliminar)
- Implementar patrones de URL RESTful para operaciones CRUD

### 2. Implementación de Vistas
- Vistas basadas en clases o funciones para operaciones CRUD
- **Cada aplicación debe tener sus propias vistas**: trabajadores, empresa, productos, proveedores
- Manejo apropiado de errores y validación
- Manejo de formularios para operaciones de crear/actualizar
- Páginas separadas para formularios de edición/creación

### 3. Templates
- Template base con navegación común
- **Templates individuales para cada operación CRUD de cada aplicación**
- Diseño responsivo usando CSS/Bootstrap
- Funcionalidad de carga y visualización de imágenes

### 4. Archivos Estáticos
- Estilos CSS para diseño responsivo
- JavaScript para UX mejorada (opcional)
- Manejo de archivos multimedia para carga de imágenes

### 5. Formularios
- **Django ModelForms para cada modelo** (Trabajador, Empresa, Producto, Proveedor)
- Validación apropiada y manejo de errores
- Manejo de carga de archivos para imágenes

## Configuración de Desarrollo
Ver sección de configuración de dependencias y migración de base de datos más adelante en este documento.

## Especificaciones de Acceso y Seguridad

**Aplicación de acceso público:**
- Todas las operaciones CRUD son públicas y accesibles para cualquier visitante
- La aplicación es completamente abierta - cualquier persona puede crear, editar, ver y eliminar cualquier registro

## Criterios de Validación
- Todas las operaciones CRUD deben ser funcionales
- La integración con base de datos debe funcionar correctamente
- Todas las páginas deben renderizar apropiadamente con navegación
- La funcionalidad de carga de imágenes debe funcionar
- Implementación de diseño responsivo
- Manejo apropiado de errores y validación
- Acceso público sin restricciones

## Notas Adicionales
- **Temática del sitio web**: {{ tipo_tienda }}
- **Paleta de colores sugerida**: Colores apropiados para el {{ tipo_tienda }} (tonos industriales, azules, grises, naranjas)
- **Contenido visual**: Las imágenes y diseño deben reflejar la estética propia del {{ tipo_tienda }} (herramientas, vehículos, equipos mecánicos)

