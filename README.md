# Sistema de Gestión Académica

## Descripción

Este proyecto implementa un sistema para la gestión de planes de estudio, carreras y materias, diseñado para ejecutarse en un entorno local. La arquitectura separa los servicios de consulta y modificación con el objetivo de mejorar la seguridad, el control de acceso y la mantenibilidad.

## Características principales

* Gestión de carreras, planes y materias
* API separada para lectura (GET) y escritura (modificación)
* Interfaz web ligera para administración
* Ejecución en entorno local controlado
* Scripts automatizados para despliegue

## Requisitos

* Linux
* Python 3.x
* Dependencias incluidas en el proyecto

## Instalación y ejecución

1. Clonar el repositorio:

   ```bash
   git clone <url-del-repo>
   cd <nombre-del-repo>
   ```

2. Ejecutar el sistema:

   ```bash
   ./init
   ```

## Scripts disponibles

* `./init`
  Inicializa el sistema por primera vez, levantando servicios necesarios.

* `./server`
  Inicia los servicios del sistema (APIs y frontend).

* `./killer`
  Detiene todos los servicios en ejecución.

## Arquitectura

El sistema se divide en:

* **API de lectura**

  * Solo métodos GET
  * Puede exponerse sin comprometer la seguridad

* **API de escritura**

  * Maneja modificaciones en la base de datos
  * Acceso restringido a entorno local

* **Frontend**

  * Interfaz web para interacción con el sistema

## Uso

1. Ejecutar `./init`
2. Acceder al frontend desde el navegador
3. Utilizar la interfaz para gestionar:

   * Carreras
   * Planes
   * Materias

## Seguridad

Las operaciones críticas (modificación de datos) están restringidas a servicios locales, evitando exposición innecesaria en red.

## Notas

* Asegúrese de tener permisos de ejecución en los scripts:

  ```bash
  chmod +x init server killer
  ```
* Para ejecutar scripts:

  ```bash
  ./nombre-del-script
  ```

## Trabajo futuro

* Implementación de autenticación
* Control de roles
* Despliegue en red segura

## Autor

Proyecto desarrollado como parte de un entorno académico.
