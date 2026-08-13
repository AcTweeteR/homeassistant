# Integration reference

This page is the repository catalog and the technical inventory for the
currently published integration. It is intended to answer two questions before
installation: what is available, and what will change in Home Assistant.

## Published integrations

| Domain | Display name | Type | Distribution | Runtime behavior |
| --- | --- | --- | --- | --- |
| `livoltek` | Livoltek | Device integration | HACS | HTTPS cloud polling |

There are no published add-ons, dashboards, cards, automations, services or
other integrations in this repository. `addons/` is intentionally empty apart
from its documentation file.

## What HACS installs

HACS copies the contents of `custom_components/livoltek/` into the Home
Assistant configuration directory. The installed package contains:

| File | Responsibility |
| --- | --- |
| `manifest.json` | Domain, version, HACS metadata, dependency and issue links |
| `__init__.py` | Integration setup, coordinator lifecycle and device registry |
| `config_flow.py` | UI setup, authentication, site selection and re-authentication |
| `const.py` | Domain, API endpoints, configuration keys and polling interval |
| `coordinator.py` | Periodic cloud polling and cached last-known values |
| `helper.py` | API client, authentication, response parsing and device helpers |
| `entity.py` | Shared coordinator-backed entity base class |
| `sensor.py` | Battery, power and daily energy sensor entities |
| `diagnostics.py` | Sanitizable Home Assistant diagnostics data |
| `strings.json` | Default config-flow and entity labels |
| `translations/en.json` | English UI translations |

No files are copied to `addons/`, no container is started and no external
service is installed.

## Entities created

The sensor platform conditionally creates the following entities when the
corresponding data is present in the Livoltek response:

| Translation key | English name | Device class | Unit | State class |
| --- | --- | --- | --- | --- |
| `battery_soc` | Battery SoC | Battery | `%` | Measurement |
| `power_grid_power` | Current Grid Import | Power | `kW` | Measurement |
| `pv_power` | Current Solar Generation | Power | `kW` | Measurement |
| `load_power` | Current Load Consumption | Power | `kW` | Measurement |
| `energy_power` | Current Battery Power | Power | `kW` | Measurement |
| `grid_import_energy` | Grid Import Today | Energy | `kWh` | Total increasing |
| `grid_export_energy` | Grid Export Today | Energy | `kWh` | Total increasing |
| `solar_generation_energy` | Solar Generation Today | Energy | `kWh` | Total increasing |

Unique IDs are derived from the selected Site ID and the sensor key. Home
Assistant therefore keeps entities stable when the display name changes.

## Runtime behavior

- Poll interval: 2 minutes and 30 seconds.
- API timeout: 30 seconds per cloud operation.
- Authentication: JWT-style access token obtained from the Livoltek API.
- Endpoint selection: EMEA or global endpoint from the setup form.
- Site selection: sites are fetched after authentication and selected in a
  dropdown.
- Night/offline handling: last valid site, device, power-flow and daily energy
  values are retained when the portal temporarily returns no data.
- Silent token expiry handling: repeated empty device lists trigger a token
  refresh attempt.
- Failure handling: cloud errors become Home Assistant update failures and are
  recorded in the integration log without exposing credentials.
- Control scope: read-only monitoring; no inverter write or control service is
  registered.

## Repository areas

| Path | Audience | Purpose |
| --- | --- | --- |
| `custom_components/livoltek/` | Home Assistant/HACS | Installable integration |
| `docs/` | Users and maintainers | Detailed documentation |
| `tests/` | Contributors | Offline automated tests |
| `config/` | Contributors | Local development configuration |
| `scripts/` | Contributors | Setup, lint and development helpers |
| `.github/workflows/` | Maintainers | HACS, Hassfest, Ruff and release automation |
| `addons/` | Future maintainers | Reserved for a future real add-on |

## Validation and release artifacts

Every push to `main` runs HACS validation, Hassfest validation and Ruff linting.
Published releases create `livoltek.zip`, containing only the integration
package. The release workflow does not package the repository documentation or
any Home Assistant backup data into the HACS archive.
