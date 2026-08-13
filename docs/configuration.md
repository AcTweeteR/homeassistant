# Livoltek configuration

Configuration is performed from the Home Assistant UI. Editing
`configuration.yaml` is not required.

## Required portal values

The Livoltek portal must provide:

| Field | Purpose | Sensitivity |
| --- | --- | --- |
| API key | Authenticates cloud API requests | Secret |
| `secuid` | User or session identifier | Sensitive |
| User token | Account/session token | Secret |
| Site ID | Selects the installation to poll | Sensitive |

Go to **Settings > Devices & services**, add the Livoltek integration and
complete the fields requested by the config flow. The integration creates one
Home Assistant device for the selected installation and polls it periodically.

## Expected behavior

- Cloud polling runs approximately every 2 minutes and 30 seconds.
- If the portal returns an empty response overnight or while the inverter is
  off, the last valid value is retained when possible.
- If the cloud session expires and repeated empty device lists are returned, the
  integration attempts token recovery before marking the device unavailable.
- Daily energy sensors use `total_increasing` so they can be used by the Home
  Assistant Energy dashboard.

## Configuration changes

To change credentials, open the Livoltek integration entry in **Settings >
Devices & services** and use its reconfigure action. Do not copy tokens into
`configuration.yaml`, issue reports or dashboard screenshots.
