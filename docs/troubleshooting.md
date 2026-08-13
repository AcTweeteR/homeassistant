# Troubleshooting

## The device is unavailable

1. Confirm that Home Assistant has Internet access.
2. Check that the API key, `secuid`, user token and Site ID are still valid in
   the Livoltek portal.
3. Open **Settings > Devices & services > Livoltek** and review diagnostics or
   use the integration's reconfigure action.
4. Check the Home Assistant log for `custom_components.livoltek` and
   `pylivoltek`.

## Data is available during the day but not at night

Some inverters or cloud portals stop returning measurements while the inverter
is off. This maintained version retains the last valid values and avoids
interpreting a temporary empty response as a permanent failure.

## The token appears to have expired

The integration attempts session recovery after repeated empty responses. If
the problem continues, generate a new token in the Livoltek portal and use the
integration's reconfigure action.

## What to include in a bug report

- Home Assistant version;
- Livoltek integration version;
- inverter model;
- approximate date and time of the failure;
- diagnostics downloaded from the integration;
- relevant sanitized log lines.

Never include API keys, tokens, passwords, complete `secuid` values or private
screenshots.
