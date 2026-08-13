# AcTweeteR Home Assistant

Resumen en español de la integración Livoltek. La documentación principal y
las instrucciones técnicas se mantienen en inglés en el [README principal](README.md).

## Instalación con HACS

[![Abrir en HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=AcTweeteR&repository=hass-livoltek&category=integration)

**[Añadir Livoltek a HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=AcTweeteR&repository=hass-livoltek&category=integration)**

1. Abre el botón anterior o entra en **HACS > Integraciones**.
2. Busca **Livoltek** y pulsa **Descargar**.
3. Reinicia Home Assistant si HACS lo solicita.
4. Ve a **Configuración > Dispositivos y servicios > Añadir integración**.
5. Busca **Livoltek** y completa el formulario.

Si no aparece en HACS, añade como repositorio personalizado:

```text
https://github.com/AcTweeteR/hass-livoltek
```

Selecciona la categoría **Integración**.

## Datos necesarios

Necesitarás la API key, `secuid`, user token y Site ID del portal Livoltek. La
integración consulta los datos del inversor mediante cloud polling y crea
sensores de batería, red, producción solar y energía diaria.

Livoltek no es un add-on. Este repositorio contiene únicamente esta integración
HACS y no instala dashboards, tarjetas Lovelace ni servicios de control del
inversor. Consulta las [guías completas en inglés](docs/README.md) para
diagnóstico, actualizaciones y soporte.
