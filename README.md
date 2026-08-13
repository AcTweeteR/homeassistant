# Home Assistant Livoltek

[![HACS validation](https://github.com/AcTweeteR/hass-livoltek/actions/workflows/validate.yml/badge.svg)](https://github.com/AcTweeteR/hass-livoltek/actions/workflows/validate.yml)
[![Lint](https://github.com/AcTweeteR/hass-livoltek/actions/workflows/lint.yml/badge.svg)](https://github.com/AcTweeteR/hass-livoltek/actions/workflows/lint.yml)
[![Latest release](https://img.shields.io/github/v/release/AcTweeteR/hass-livoltek?display_name=tag&sort=semver)](https://github.com/AcTweeteR/hass-livoltek/releases)
[![HACS](https://img.shields.io/badge/HACS-custom%20integration-41BDF5.svg)](https://hacs.xyz/)
[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-integration-18BCF2.svg)](https://www.home-assistant.io/)
[![License](https://img.shields.io/github/license/AcTweeteR/hass-livoltek)](LICENSE)

Home Assistant custom integration for monitoring Livoltek inverter installations
through the Livoltek cloud portal. This repository contains one integration,
`livoltek`, maintained for current Home Assistant releases and distributed
through HACS.

## Add Livoltek to HACS

[![Add this repository to HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=AcTweeteR&repository=hass-livoltek&category=integration)

**[Add Livoltek to HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=AcTweeteR&repository=hass-livoltek&category=integration)**

1. Open the button above or go to **HACS > Integrations**.
2. Search for **Livoltek** and select **Download**.
3. Restart Home Assistant if HACS requests it.
4. Open **Settings > Devices & services > Add integration**.
5. Search for **Livoltek** and complete the configuration flow.

If it is not yet visible in the HACS catalog, add this repository under
**HACS > Integrations > three-dot menu > Custom repositories** with category
**Integration**:

```text
https://github.com/AcTweeteR/hass-livoltek
```

## What this repository contains

| Domain | Name | Type | Distribution |
| --- | --- | --- | --- |
| `livoltek` | Livoltek | Read-only cloud device integration | HACS |

This repository contains no add-ons, dashboards, Lovelace cards, automations,
Docker containers or inverter control services. HACS installs only the
`custom_components/livoltek/` package into the Home Assistant configuration
directory.

### Installed package

| File | Purpose |
| --- | --- |
| `manifest.json` | Integration domain, version, dependency and support links |
| `__init__.py` | Config-entry setup, unload and device registration |
| `config_flow.py` | UI setup, authentication, site selection and re-authentication |
| `const.py` | API endpoints, configuration keys and polling interval |
| `coordinator.py` | Periodic cloud polling and last-known-value retention |
| `helper.py` | API client, authentication and defensive response parsing |
| `entity.py` | Shared coordinator-backed entity behavior |
| `sensor.py` | Battery, power and daily energy sensors |
| `diagnostics.py` | Home Assistant diagnostics support |
| `strings.json` / `translations/en.json` | Configuration and entity labels |

## Features

- UI-based setup with no `configuration.yaml` changes.
- Livoltek EMEA and global cloud endpoint selection.
- Site discovery after authentication and per-site configuration.
- Read-only monitoring with no inverter write commands or control services.
- Approximately 2 minute 30 second polling interval.
- 30 second API operation timeout to avoid blocking Home Assistant.
- Last valid data retained when the inverter is offline or the cloud response is
  temporarily empty.
- Token refresh recovery after repeated empty device responses.
- Home Assistant diagnostics support.
- Daily energy sensors marked `total_increasing` for the Energy dashboard.

## Entities

Entities are created when the corresponding value is present in the Livoltek
response. Names are translated by Home Assistant and may include the selected
site name.

| Entity | Unit | Device class | State class | Description |
| --- | --- | --- | --- | --- |
| Battery SoC | `%` | Battery | Measurement | Battery state of charge |
| Current Grid Import | `kW` | Power | Measurement | Instantaneous grid power |
| Current Solar Generation | `kW` | Power | Measurement | Instantaneous PV production |
| Current Load Consumption | `kW` | Power | Measurement | Current household/load power |
| Current Battery Power | `kW` | Power | Measurement | Current battery power |
| Grid Import Today | `kWh` | Energy | Total increasing | Daily grid import |
| Grid Export Today | `kWh` | Energy | Total increasing | Daily grid export |
| Solar Generation Today | `kWh` | Energy | Total increasing | Daily solar generation |

Unique IDs are derived from the selected Site ID and sensor key, so entity
identity remains stable when the display name changes.

## Configuration

The config flow requires values from the Livoltek portal:

| Field | Purpose |
| --- | --- |
| API key | Authenticates cloud API requests |
| `secuid` | Account or session security identifier |
| User token | Token generated by the Livoltek portal |
| Use EMEA server | Selects the European API endpoint when applicable |
| Site | Livoltek installation selected after authentication |

The integration stores these values in Home Assistant's protected config-entry
storage. It does not open inbound ports, start a local service or execute
inverter control commands.

## Compatibility

| Requirement | Value |
| --- | --- |
| Home Assistant | `2024.12.0` or newer according to HACS metadata |
| Integration version | See the latest release |
| Python dependency | `pylivoltek==1.0.9` |
| Network | Home Assistant requires Internet access |
| Connection | Livoltek cloud polling over HTTPS |

## Documentation

| Guide | Contents |
| --- | --- |
| [Installation](docs/installation.md) | HACS and custom repository setup |
| [Configuration](docs/configuration.md) | Credentials and polling behavior |
| [Entities and sensors](docs/sensors.md) | Measurements and Energy dashboard |
| [Integration reference](docs/integration-reference.md) | Complete file and runtime inventory |
| [Troubleshooting](docs/troubleshooting.md) | Common failures and safe diagnostics |
| [Maintenance](docs/maintenance.md) | Updates, backups, rollback and security |
| [Development](docs/development.md) | Repository layout and validation |
| [Changelog](CHANGELOG.md) | Release history |
| [Contributing](CONTRIBUTING.md) | Issues, pull requests and coding style |
| [Security policy](SECURITY.md) | Sensitive data and vulnerability reports |

## Spanish

See [README.es.md](README.es.md) for a short Spanish installation and feature
summary. The maintained technical documentation is written in English first.

## Attribution

This maintained version is based on
[hass-livoltek](https://github.com/adamlonsdale/hass-livoltek) by Adam Lonsdale
and remains under the MIT license. Original attribution is preserved in
[LICENSE](LICENSE).

## Support and privacy

For issues, include the Home Assistant version, integration version, inverter
model, approximate failure time and sanitized diagnostics. Never publish API
keys, tokens, passwords, complete `secuid` values or Home Assistant backups.

Use the repository [Issues](https://github.com/AcTweeteR/hass-livoltek/issues)
for questions and feature proposals.
