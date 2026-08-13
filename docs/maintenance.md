# Mantenimiento

## Actualizar con HACS

HACS mostrará las nuevas versiones en su panel de actualizaciones. Revisa el
`CHANGELOG.md`, actualiza la integración y reinicia Home Assistant si HACS lo
indica.

## Antes de actualizar

- Comprueba que existe una copia de seguridad reciente de Home Assistant.
- Anota la versión actual de Home Assistant y Livoltek.
- Revisa los cambios de `CHANGELOG.md`.

## Volver atrás

Si una versión provoca un problema, utiliza la opción de descarga de versión
de HACS para instalar la última versión conocida como estable y reinicia Home
Assistant. Conserva los datos de configuración de la integración antes de
eliminar una entrada.

## Seguridad

La integración consulta el servicio cloud de Livoltek. No contiene credenciales
predeterminadas, no abre puertos entrantes y no ejecuta órdenes sobre el
inversor. Protege especialmente los tokens y las copias de seguridad de Home
Assistant.
