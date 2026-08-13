# Seguridad

## Comunicación de vulnerabilidades

No publiques vulnerabilidades con credenciales, tokens o datos privados en
Issues. Utiliza la función de aviso privado de seguridad de GitHub o contacta
con el mantenedor desde el perfil del repositorio.

## Datos sensibles

La integración necesita credenciales del portal cloud de Livoltek para
consultar datos. Esos valores se almacenan en la configuración protegida de
Home Assistant y no deben incluirse en incidencias, logs compartidos,
capturas, pull requests ni copias públicas.

La integración no incluye credenciales predeterminadas, no abre puertos
entrantes y no ejecuta órdenes de control sobre el inversor: su función es
consultar datos del servicio cloud configurado.
