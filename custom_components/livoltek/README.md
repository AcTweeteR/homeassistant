# Livoltek integration package

This directory contains the Home Assistant integration package: Python setup,
config flow, coordinator, entities, diagnostics, translations and manifest.

The package implements one read-only device integration for Livoltek cloud
portals. It creates eight conditional sensor types: battery state, current grid
power, solar generation power, load consumption, battery power, daily grid
import, daily grid export and daily solar generation. It does not provide
switches, number entities, services, automations, dashboards or inverter
control commands.

User documentation is maintained at repository level:

- [Installation](../../docs/installation.md)
- [Configuration](../../docs/configuration.md)
- [Entities and sensors](../../docs/sensors.md)
- [Troubleshooting](../../docs/troubleshooting.md)

This directory must be installed as `custom_components/livoltek/` by HACS. It
is not a Home Assistant OS add-on and must not be copied into `addons/`.
