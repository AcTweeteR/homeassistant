# Desarrollo

## Estructura del repositorio

```text
custom_components/livoltek/  Integración de Home Assistant
tests/                        Pruebas automatizadas
addons/                       Espacio reservado para futuros complementos
docs/                         Documentación de usuario y mantenimiento
.github/workflows/            Validación, lint y publicación de releases
```

## Validaciones locales

```bash
python3 -m ruff check .
pytest
```

Antes de abrir una pull request, actualiza la documentación y el changelog.
Los cambios de comportamiento de la integración deben incluir pruebas cuando
sea posible.

## Añadir un futuro complemento

Si algún día se publica un complemento real, crea `addons/<slug>/config.yaml` y
añade todos los archivos necesarios para construirlo y ejecutarlo. En ese
momento habrá que añadir de nuevo la metadata de repositorio para la tienda de
Home Assistant OS y documentar su instalación y permisos en un README propio.
No coloques copias de seguridad ni carpetas temporales dentro de `addons/`.
