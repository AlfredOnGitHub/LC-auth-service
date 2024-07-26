# LC-ORG-SERVICE

Microservicio de Gestión de Organizaciones

Este microservicio gestiona organizaciones y usuarios asociados.

## Requisitos

- Docker
- Docker Compose (opcional)
- Python 3.11 (si no usas Docker)

## Instalación

1. Clonar el repositorio:
   ```
   git clone https://github.com/AlfredOnGitHub/gestion-organizaciones.git
   cd gestion-organizaciones
    ```
2. Configurar las variables de entorno:
    Crea un archivo .env basado en .env.example y configura las variables necesarias.

3. Construir la imagen Docker:
    ```
    docker build -t org_service .
    ```

4. Ejecutar el contenedor:

    ```
    docker run -p 8000:8000 org_service
    ```

### Se puede comprobar su funcionamiento en local accediendo a 127.0.0.0:8000

## Contribución

SOON.