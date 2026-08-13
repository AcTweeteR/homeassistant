# Instalación

## Integración Livoltek con HACS

La integración es una integración personalizada de Home Assistant, no un
add-on. HACS instala sus archivos en `custom_components/livoltek/`.

### Instalación rápida

[![Añadir a HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=AcTweeteR&repository=homeassistant&category=integration)

1. Abre el enlace anterior o entra en **HACS > Integraciones**.
2. Busca **Livoltek**.
3. Pulsa **Descargar** y reinicia Home Assistant cuando HACS lo solicite.
4. Ve a **Configuración > Dispositivos y servicios > Añadir integración**.
5. Busca **Livoltek** y completa el formulario.

### Repositorio personalizado

Si Livoltek todavía no aparece en el catálogo de HACS:

1. Abre **HACS > Integraciones > menú de tres puntos > Repositorios personalizados**.
2. Añade `https://github.com/AcTweeteR/homeassistant`.
3. Selecciona la categoría **Integración**.
4. Instala **Livoltek** y reinicia Home Assistant.

## Futuros complementos

Actualmente este repositorio no se publica como repositorio de la tienda de
complementos. Livoltek es una integración HACS y no aparecerá en esa tienda.
Si en el futuro se añade un complemento real dentro de `addons/`, se publicará
entonces la metadata oficial y se documentará su instalación por separado.
