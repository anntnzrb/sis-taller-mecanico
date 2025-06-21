# Pseudocode Architecture - Taller Mecánico System

## System Architecture Overview

### 1. Django App Structure
```
MAIN_PROJECT: taller_mecanico
├── APPS:
│   ├── trabajadores/     # Worker management
│   ├── empresa/         # Company management  
│   ├── productos/       # Product management
│   └── proveedores/     # Supplier management
├── SHARED:
│   ├── templates/       # HTML templates
│   ├── static/         # CSS, JS, images
│   └── media/          # User uploads
```

### 2. Data Flow Architecture
```
HTTP_REQUEST → URL_DISPATCHER → VIEW → MODEL → DATABASE
                                  ↓
              TEMPLATE ← CONTEXT ←
```

## Core Business Logic Algorithms

### 1. Entity CRUD Operations Pattern
```python
class EntityCRUDService:
    def list_entities():
        # Query all entities from database
        # Apply any filtering/ordering
        # Return queryset for template
        
    def create_entity(form_data):
        # Validate form data
        # Create new entity instance
        # Save to database
        # Handle file uploads (images)
        # Return success/error status
        
    def update_entity(entity_id, form_data):
        # Get entity by ID or 404
        # Validate form data
        # Update entity fields
        # Handle file uploads
        # Save changes
        # Return success/error status
        
    def delete_entity(entity_id):
        # Get entity by ID or 404
        # Delete associated files
        # Delete from database
        # Return success status
```

### 2. Company Management (Single Instance)
```python
class CompanyService:
    def get_or_create_company():
        # Check if company exists
        # If exists: return company instance
        # If not: return None for create form
        
    def has_company_info():
        # Boolean check for company existence
        # Used for conditional UI rendering
```

### 3. Image Handling Algorithm
```python
class ImageService:
    def process_upload(image_file):
        # Validate file type and size
        # Generate unique filename
        # Save to media directory
        # Return file path or error
        
    def get_image_url(entity):
        # If entity has image: return URL
        # Else: return placeholder URL
```

### 4. Form Validation Strategy
```python
class FormValidationService:
    def validate_trabajador(data):
        # Validate email format
        # Check cedula uniqueness
        # Validate codigo_empleado format
        
    def validate_producto(data):
        # Validate price is positive
        # Ensure IVA is 0 or 15
        # Check required fields
        
    def validate_proveedor(data):
        # Validate email format
        # Validate phone format
        # Check required fields
```

## Test Strategy (TDD London School)

### 1. Unit Testing Approach
```python
class ModelTestSuite:
    def test_model_creation():
        # Test model instance creation
        # Verify field validation
        # Test model methods
        
    def test_model_constraints():
        # Test database constraints
        # Test unique fields
        # Test required fields

class ViewTestSuite:
    def test_crud_operations():
        # Test GET requests return correct templates
        # Test POST requests create/update entities
        # Test DELETE requests remove entities
        # Test form validation
        
    def test_authentication_not_required():
        # Verify all views are publicly accessible
        
class FormTestSuite:
    def test_form_validation():
        # Test valid data passes
        # Test invalid data fails
        # Test error messages
```

### 2. Integration Testing Strategy
```python
class IntegrationTestSuite:
    def test_full_crud_workflow():
        # Create entity via form
        # Read entity in list view
        # Update entity via form
        # Delete entity
        
    def test_image_upload_workflow():
        # Upload image with entity
        # Verify image saved correctly
        # Verify image displays in templates
        
    def test_company_single_instance_logic():
        # Test creation when no company exists
        # Test edit when company exists
        # Test UI state changes
```

### 3. End-to-End Testing Scenarios
```python
class E2ETestSuite:
    def test_worker_management():
        # Navigate to workers page
        # Add new worker with image
        # Edit worker information
        # Delete worker
        
    def test_product_catalog():
        # Navigate to products page
        # Add product with pricing
        # Test IVA calculation display
        # Edit and delete product
        
    def test_navigation_flow():
        # Test all navigation links work
        # Test responsive design
        # Test form submissions
```

## Error Handling & Recovery Strategy

### 1. Database Error Handling
```python
class DatabaseErrorHandler:
    def handle_connection_error():
        # Log error details
        # Display user-friendly message
        # Attempt reconnection
        
    def handle_constraint_violation():
        # Identify constraint type
        # Return specific error message
        # Suggest correction
```

### 2. File Upload Error Handling
```python
class FileUploadErrorHandler:
    def handle_invalid_file_type():
        # Validate file extension
        # Return specific error message
        
    def handle_file_size_limit():
        # Check file size
        # Return size limit message
        
    def handle_storage_error():
        # Log storage issue
        # Fallback to default placeholder
```

### 3. Form Validation Error Strategy
```python
class FormErrorHandler:
    def collect_form_errors():
        # Aggregate all field errors
        # Format for template display
        # Preserve form data
        
    def handle_unique_constraint_errors():
        # Detect duplicate values
        # Return user-friendly message
        # Highlight problematic fields
```

## Performance Optimization Strategies

### 1. Database Query Optimization
```python
class QueryOptimizer:
    def optimize_list_queries():
        # Use select_related for ForeignKeys
        # Use prefetch_related for reverse relations
        # Implement pagination for large datasets
        
    def optimize_image_queries():
        # Lazy load images
        # Implement image caching
        # Optimize image sizes
```

### 2. Caching Strategy
```python
class CacheManager:
    def cache_static_content():
        # Cache company information
        # Cache navigation data
        # Set appropriate cache headers
        
    def cache_template_fragments():
        # Cache expensive template rendering
        # Invalidate on data changes
```

## Security Implementation

### 1. Input Validation
```python
class SecurityValidator:
    def validate_all_inputs():
        # Django form validation
        # SQL injection prevention
        # XSS prevention through escaping
        
    def validate_file_uploads():
        # File type validation
        # File size limits
        # Malicious file detection
```

### 2. CSRF Protection
```python
class CSRFProtection:
    def protect_all_forms():
        # Include CSRF tokens in all forms
        # Validate tokens on submission
        # Handle CSRF failures gracefully
```

Target: 80% test coverage with comprehensive validation and error handling