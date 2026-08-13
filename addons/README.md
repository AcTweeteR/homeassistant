# Complementos de Home Assistant OS

Esta carpeta queda reservada para futuros add-ons mantenidos en este repositorio.
Actualmente no forma parte de la distribución de la integración Livoltek ni se
publica como repositorio de la tienda de complementos.

Actualmente no hay ningún add-on publicado aquí. Livoltek es una integración de
HACS y no debe copiarse a esta carpeta.

Cada futuro add-on deberá tener una carpeta propia, por ejemplo
`addons/mi_addon/`, con al menos:

- `config.yaml`, con los metadatos oficiales del add-on;
- `Dockerfile` o una imagen válida;
- `README.md`, con instalación, configuración, permisos y soporte;
- todos los archivos necesarios para construirlo y ejecutarlo.

No guardes copias de seguridad, builds ni carpetas temporales bajo `addons/`.
