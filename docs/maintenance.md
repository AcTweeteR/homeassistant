# Maintenance

## Update with HACS

HACS exposes new releases in its update panel. Review `CHANGELOG.md`, update
the integration and restart Home Assistant when HACS requests it.

## Before updating

- Confirm that a recent Home Assistant backup exists.
- Record the current Home Assistant and Livoltek versions.
- Review the release notes in `CHANGELOG.md`.

## Roll back

If a release causes a problem, use HACS's version selector to install the last
known-good release and restart Home Assistant. Keep the integration's device
configuration intact unless the issue explicitly requires reconfiguration.

## Security and privacy

The integration queries Livoltek's cloud service. It has no default credentials,
opens no inbound ports and does not send inverter control commands. Protect
tokens, diagnostics and Home Assistant backups as private data.
