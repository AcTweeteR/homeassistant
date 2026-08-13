# Entities and sensors

The integration creates sensors associated with the Livoltek device. Exact
entity names depend on the installation name and data returned by the portal.

| Measurement | Unit | Description |
| --- | --- | --- |
| Battery state | `%` | Battery state of charge |
| Grid power | `kW` | Import or export power at the grid connection |
| PV power | `kW` | Instantaneous solar production |
| Charge power | `kW` | Power sent to charge the battery |
| Energy power | `kW` | Energy power reported by the portal |
| Grid import energy | `kWh` | Daily energy imported from the grid |
| Grid export energy | `kWh` | Daily energy exported to the grid |
| Solar generation | `kWh` | Daily solar energy generation |

Daily energy sensors are prepared for the Home Assistant Energy dashboard. Their
availability depends on the portal providing data for the selected device and
period.

## Availability and historical data

Some Livoltek inverters stop reporting when they are powered down overnight.
The integration keeps the last valid value when possible, but it cannot create
new measurements while the cloud service provides no data. This is different
from a live network failure and should be interpreted alongside the sensor
availability state.
