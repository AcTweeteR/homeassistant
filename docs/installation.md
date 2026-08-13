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

## Tienda de complementos de Home Assistant OS

[![Añadir repositorio de complementos](https://my.home-assistant.io/badges/supervisor_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FAcTweeteR%2Fhomeassistant)

El repositorio incluye `repository.yaml` y puede añadirse desde **Configuración
> Complementos > Tienda de complementos > menú de tres puntos > Repositorios**.

Esta vía es independiente de HACS. Livoltek no aparecerá como complemento,
porque es una integración que se instala en `custom_components/`. Solo los
futuros proyectos con una carpeta propia dentro de `addons/` y un `config.yaml`
válido aparecerán como complementos instalables.
