# Home Assistant Custom Repository

Repositorio de integraciones y futuros add-ons de Home Assistant mantenidos por
AcTweeteR. La primera integración publicada es Livoltek, una adaptación de
`hass-livoltek` para versiones actuales de Home Assistant.

[![HACS validation](https://github.com/AcTweeteR/homeassistant/actions/workflows/validate.yml/badge.svg)](https://github.com/AcTweeteR/homeassistant/actions/workflows/validate.yml)
[![License](https://img.shields.io/github/license/AcTweeteR/homeassistant)](LICENSE)

## Añadirlo a Home Assistant

### HACS

[![Abrir en HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=AcTweeteR&repository=homeassistant&category=integration)

También se puede añadir manualmente en HACS como repositorio personalizado:

1. Abrir HACS y entrar en **Integraciones**.
2. Abrir el menú de tres puntos y elegir **Repositorios personalizados**.
3. Añadir `https://github.com/AcTweeteR/homeassistant` con categoría **Integración**.
4. Buscar **Livoltek** e instalarla.

### Repositorio de add-ons

[![Añadir repositorio de add-ons](https://my.home-assistant.io/badges/supervisor_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FAcTweeteR%2Fhomeassistant)

El repositorio incluye la carpeta `addons/` reservada para futuras aplicaciones.
Actualmente no contiene un add-on instalable; cuando se publique el primero se
podrá instalar desde **Configuración > Add-ons > Repositorios**.

## Livoltek

La integración consulta el portal cloud de Livoltek y crea sensores de:

| Sensor | Unidad o significado |
| --- | --- |
| Estado de batería | Porcentaje |
| Potencia de red | kW |
| Potencia fotovoltaica | kW |
| Potencia de carga | kW |
| Potencia energética | kW |
| Energía importada de red | kWh diarios |
| Energía exportada a red | kWh diarios |
| Generación solar | kWh diarios |

La configuración se realiza desde **Configuración > Dispositivos y servicios**.
Se necesita la API key, el `secuid`, el user token y el identificador del sitio
que proporciona el portal Livoltek.

### Cambios de esta adaptación

- Compatibilidad con las APIs actuales de Home Assistant.
- Coordinador basado en `DataUpdateCoordinator` con intervalo de 2 minutos y 30 segundos.
- Timeouts para evitar bloqueos del ciclo de Home Assistant.
- Renovación del token cuando el portal devuelve listas vacías tras caducar la sesión.
- Conservación del último dato válido cuando el inversor está apagado o el portal no devuelve datos temporales.
- Validación más defensiva de respuestas del portal y diagnósticos de la integración.
- Sensores de energía diaria con estado `total_increasing`.

La adaptación parte del proyecto original de Adam Lonsdale:
[adamlonsdale/hass-livoltek](https://github.com/adamlonsdale/hass-livoltek),
publicado bajo licencia MIT. Se mantiene la atribución original en
[LICENSE](LICENSE).

## Actualizaciones

Una vez instalada mediante HACS, las nuevas versiones se ofrecerán desde el
gestor de actualizaciones de HACS. Las actualizaciones solo cambian los
archivos de la integración y no eliminan la configuración de los dispositivos.

## Diagnóstico y contribuciones

Para informar de un problema, incluye la versión de Home Assistant, la versión
de la integración, el modelo del inversor y los diagnósticos generados desde la
integración. No publiques API keys, tokens ni capturas que los contengan.

Las contribuciones son bienvenidas. Consulta [CONTRIBUTING.md](CONTRIBUTING.md)
antes de abrir una pull request.
