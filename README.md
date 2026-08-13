# AcTweeteR Home Assistant

[![HACS validation](https://github.com/AcTweeteR/homeassistant/actions/workflows/validate.yml/badge.svg)](https://github.com/AcTweeteR/homeassistant/actions/workflows/validate.yml)
[![Lint](https://github.com/AcTweeteR/homeassistant/actions/workflows/lint.yml/badge.svg)](https://github.com/AcTweeteR/homeassistant/actions/workflows/lint.yml)
[![Latest release](https://img.shields.io/github/v/release/AcTweeteR/homeassistant?display_name=tag&sort=semver)](https://github.com/AcTweeteR/homeassistant/releases)
[![HACS](https://img.shields.io/badge/HACS-custom%20integration-41BDF5.svg)](https://hacs.xyz/)
[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-custom%20integration-18BCF2.svg)](https://www.home-assistant.io/)
[![License](https://img.shields.io/github/license/AcTweeteR/homeassistant)](LICENSE)

Public repository for Home Assistant integrations maintained by **AcTweeteR**.
The first published project is the Livoltek cloud integration, maintained for
current Home Assistant releases and distributed through HACS.

| Project | Distribution | Status |
| --- | --- | --- |
| **Livoltek** integration | HACS | Available |
| Future Home Assistant OS add-ons | Home Assistant add-on store | Not published |

> **Important:** Livoltek is a Home Assistant integration, not an add-on. It
> belongs in `custom_components/` and must be installed through HACS.

## Quick start

### Install Livoltek with HACS

[![Add this repository to HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=AcTweeteR&repository=homeassistant&category=integration)

**[Add Livoltek to HACS](https://my.home-assistant.io/redirect/hacs_repository/?owner=AcTweeteR&repository=homeassistant&category=integration)**

1. Open the button above or go to **HACS > Integrations**.
2. Search for **Livoltek** and select **Download**.
3. Restart Home Assistant if HACS requests it.
4. Open **Settings > Devices & services > Add integration**.
5. Search for **Livoltek** and complete the configuration form.

If the integration is not yet visible in the HACS catalog, add this repository
manually under **HACS > Integrations > three-dot menu > Custom repositories**
with category **Integration**:

```text
https://github.com/AcTweeteR/homeassistant
```

### What will be installed

HACS installs only the `custom_components/livoltek/` integration package. It
does not install an add-on, Docker container, dashboard, external service or
background process. The package contains the config flow, cloud API client
adapter, coordinator, sensor platform, diagnostics and English translations.

This repository currently contains **one installable Home Assistant
integration: Livoltek**. The `addons/` directory is documentation for possible
future work only and is not an installable product.

### Spanish quick start

See [README.es.md](README.es.md) for the Spanish installation summary.

## Livoltek integration

Livoltek connects to the vendor cloud portal and creates one Home Assistant
device with battery, grid, solar and daily energy sensors. Configuration is
performed from the Home Assistant UI; editing `configuration.yaml` is not
required.

### Required portal values

The Livoltek portal must provide the following values for the installation:

| Field | Purpose | Secret |
| --- | --- | --- |
| API key | Authenticates API requests | Yes |
| `secuid` | User or session identifier | Treat as sensitive |
| User token | Account/session token | Yes |
| Site ID | Selects the installation to poll | Treat as sensitive |

The integration uses these values only to query the configured Livoltek cloud
API. It does not open inbound ports and does not execute inverter commands.

### Entities and measurements

| Entity data | Unit | Description |
| --- | --- | --- |
| Battery state | `%` | Battery state of charge |
| Grid power | `kW` | Instantaneous import or export power |
| PV power | `kW` | Instantaneous solar production |
| Charge power | `kW` | Power sent to the battery |
| Energy power | `kW` | Energy power reported by the portal |
| Grid import energy | `kWh` | Daily energy imported from the grid |
| Grid export energy | `kWh` | Daily energy exported to the grid |
| Solar generation | `kWh` | Daily solar energy generation |

Daily energy sensors use the `total_increasing` state class and can be selected
for the Home Assistant Energy dashboard. Exact entity names depend on the
installation name and the device data returned by the portal.

### Maintained behavior

- Modern Home Assistant config flow and diagnostics support.
- `DataUpdateCoordinator` polling approximately every 2 minutes and 30 seconds.
- Network timeouts to avoid blocking Home Assistant's main event loop.
- Token refresh recovery after repeated empty device responses.
- Retention of the last valid values when the inverter is off or the portal
  temporarily returns an empty response.
- Defensive handling of incomplete or unexpected cloud responses.
- Daily energy sensors compatible with the Energy dashboard.

The maintained version is based on [hass-livoltek](https://github.com/adamlonsdale/hass-livoltek)
by Adam Lonsdale and remains under the MIT license. Original attribution is
preserved in [LICENSE](LICENSE).

### Compatibility and requirements

| Requirement | Current value |
| --- | --- |
| Home Assistant | `2024.12.0` or newer according to HACS metadata |
| Integration version | `1.0.2` |
| Python dependency | `pylivoltek==1.0.9` |
| Connection type | Livoltek cloud polling over HTTPS |
| Local network requirement | None; Home Assistant needs Internet access |
| Control commands | Not implemented; read-only data polling |

The integration supports the Livoltek EMEA and global API endpoints. During
setup, it authenticates the account, retrieves the available sites and lets the
user select the site to add. A site can only be configured once in the same
Home Assistant instance.

### Configuration flow fields

| Field | Displayed purpose |
| --- | --- |
| API Key | API credential issued by Livoltek |
| Security ID (`secuid`) | Account or session security identifier |
| User Token | Token generated by the Livoltek portal |
| Use EMEA Server | Selects the European API endpoint when applicable |
| Site | Livoltek installation selected after authentication |

The integration stores the configuration in Home Assistant's config-entry
storage. It does not require YAML configuration.

## Documentation

| Document | Contents |
| --- | --- |
| [Installation](docs/installation.md) | HACS and custom repository setup |
| [Configuration](docs/configuration.md) | Credentials and cloud polling behavior |
| [Entities and sensors](docs/sensors.md) | Measurements, units and Energy dashboard |
| [Troubleshooting](docs/troubleshooting.md) | Common failures and safe diagnostics |
| [Maintenance](docs/maintenance.md) | Updates, rollback and security |
| [Development](docs/development.md) | Repository layout and validation |
| [Integration reference](docs/integration-reference.md) | Complete file and behavior inventory |
| [Changelog](CHANGELOG.md) | Release history |
| [Contributing](CONTRIBUTING.md) | Issues, pull requests and coding style |
| [Security policy](SECURITY.md) | Sensitive data and vulnerability reports |

## Repository layout

```text
custom_components/livoltek/  HACS integration source and manifest
tests/                        Automated tests without real credentials
addons/                       Reserved for a future real add-on
docs/                         User, support and developer documentation
.github/                      Workflows and issue templates
config/                       Example development Home Assistant config
scripts/                      Development and validation utilities
```

See the [complete integration reference](docs/integration-reference.md) for a
description of every installable component and source area.

## Updates and support

HACS exposes new releases in its update panel. Before updating, review
[CHANGELOG.md](CHANGELOG.md) and keep a recent Home Assistant backup. For an
issue, include the Home Assistant version, integration version, inverter model,
approximate failure time and a sanitized diagnostic report.

Never publish API keys, tokens, passwords, complete `secuid` values or backups
in issues or pull requests. Use the repository
[Issues](https://github.com/AcTweeteR/homeassistant/issues) for questions and
feature proposals.
