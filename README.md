# AcTweeteR Home Assistant

[![HACS validation](https://github.com/AcTweeteR/homeassistant/actions/workflows/validate.yml/badge.svg)](https://github.com/AcTweeteR/homeassistant/actions/workflows/validate.yml)
[![Lint](https://github.com/AcTweeteR/homeassistant/actions/workflows/lint.yml/badge.svg)](https://github.com/AcTweeteR/homeassistant/actions/workflows/lint.yml)
[![Latest release](https://img.shields.io/github/v/release/AcTweeteR/homeassistant?display_name=tag&sort=semver)](https://github.com/AcTweeteR/homeassistant/releases)
[![HACS](https://img.shields.io/badge/HACS-custom%20integration-41BDF5.svg)](https://hacs.xyz/)
[![License](https://img.shields.io/github/license/AcTweeteR/homeassistant)](LICENSE)

Repositorio público para integraciones de Home Assistant mantenidas por
**AcTweeteR**. La integración Livoltek se distribuye mediante HACS.

| Proyecto | Instalación | Estado |
| --- | --- | --- |
| Integración **Livoltek** | HACS | Disponible |

> **Importante:** Livoltek es una integración de Home Assistant, no un add-on.
> Se instala con HACS.

## Instalación rápida

### Livoltek con HACS

[![Abrir en HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=AcTweeteR&repository=homeassistant&category=integration)

1. Abre el botón anterior o entra en **HACS > Integraciones**.
2. Busca **Livoltek** y pulsa **Descargar**.
3. Reinicia Home Assistant si HACS lo solicita.
4. Ve a **Configuración > Dispositivos y servicios > Añadir integración**.
5. Busca **Livoltek** y completa el formulario.

Si todavía no aparece en el catálogo de HACS, añade manualmente este
repositorio desde **HACS > Integraciones > menú de tres puntos > Repositorios
personalizados**, con categoría **Integración**:

```text
https://github.com/AcTweeteR/homeassistant
```

## Integración Livoltek

Livoltek consulta el portal cloud del inversor y crea un dispositivo con
sensores de producción, red, batería y energía diaria. La configuración se
realiza íntegramente desde la interfaz de Home Assistant; no es necesario
editar `configuration.yaml`.

### Datos necesarios

El portal debe proporcionar la API key, el `secuid`, el user token y el Site ID
de la instalación. La integración usa esos datos únicamente para consultar la
API cloud configurada por el usuario.

### Sensores

| Sensor | Unidad | Significado |
| --- | --- | --- |
| Estado de batería | `%` | Nivel de carga de la batería |
| Potencia de red | `kW` | Importación o exportación instantánea |
| Potencia fotovoltaica | `kW` | Producción solar instantánea |
| Potencia de carga | `kW` | Potencia destinada a la batería |
| Potencia energética | `kW` | Potencia energética comunicada por el portal |
| Energía importada de red | `kWh` | Acumulado diario de importación |
| Energía exportada a red | `kWh` | Acumulado diario de exportación |
| Generación solar | `kWh` | Acumulado diario de generación |

Los sensores diarios están marcados como `total_increasing` y pueden utilizarse
en el panel Energía de Home Assistant.

### Adaptaciones incluidas

- Compatibilidad con las APIs actuales de Home Assistant.
- Flujo de configuración moderno y diagnóstico de la integración.
- `DataUpdateCoordinator` con consulta aproximada cada 2 minutos y 30 segundos.
- Timeouts para evitar bloqueos del ciclo principal de Home Assistant.
- Renovación del token tras respuestas vacías repetidas del portal.
- Conservación del último dato válido cuando el inversor está apagado o el
  portal entrega una respuesta temporalmente vacía.
- Validación defensiva de respuestas incompletas o inesperadas.
- Sensores diarios de energía compatibles con el panel Energía.

La adaptación parte de [hass-livoltek](https://github.com/adamlonsdale/hass-livoltek),
de Adam Lonsdale, bajo licencia MIT. La atribución y la licencia se conservan
en [LICENSE](LICENSE).

## Documentación

| Documento | Contenido |
| --- | --- |
| [Instalación](docs/installation.md) | HACS y repositorios personalizados |
| [Configuración](docs/configuration.md) | Credenciales y comportamiento cloud |
| [Entidades](docs/sensors.md) | Sensores, unidades y panel Energía |
| [Diagnóstico](docs/troubleshooting.md) | Problemas frecuentes y datos seguros para soporte |
| [Mantenimiento](docs/maintenance.md) | Actualización, rollback y seguridad |
| [Desarrollo](docs/development.md) | Estructura, validaciones y futuros add-ons |
| [Changelog](CHANGELOG.md) | Historial de versiones |
| [Contribuir](CONTRIBUTING.md) | Issues, pull requests y estilo de código |

## Estructura del repositorio

```text
custom_components/livoltek/  Código de la integración HACS
tests/                        Pruebas automatizadas sin credenciales reales
addons/                       Espacio reservado para futuros complementos
docs/                         Documentación de instalación y mantenimiento
.github/                      Workflows, plantillas de issues y automatización
config/                       Configuración de ejemplo para desarrollo
scripts/                      Utilidades de desarrollo y validación
```

Cada área tiene una descripción local cuando contiene varios archivos. Consulta
[docs/README.md](docs/README.md) para el índice completo.

## Actualizaciones y soporte

HACS ofrece las nuevas releases desde su panel de actualizaciones. Antes de
actualizar, revisa [CHANGELOG.md](CHANGELOG.md) y conserva una copia de
seguridad reciente de Home Assistant. Para informar de un problema, incluye
las versiones de Home Assistant y Livoltek, el modelo del inversor, la hora del
fallo y un diagnóstico sin secretos.

No publiques API keys, tokens, contraseñas, `secuid` completos ni copias de
seguridad en issues o pull requests. Las dudas y propuestas se gestionan en
[Issues](https://github.com/AcTweeteR/homeassistant/issues).
