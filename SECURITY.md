# Security policy

## Reporting vulnerabilities

Do not publish vulnerabilities together with credentials, tokens or private
data in a public issue. Use GitHub's private security reporting feature or
contact the maintainer through the repository profile.

## Sensitive data

The integration requires Livoltek cloud credentials to query measurements.
These values are stored by Home Assistant's protected configuration and must
not be included in issues, shared logs, screenshots, pull requests or public
backups.

The integration has no default credentials, opens no inbound ports and does
not execute inverter control commands. Its purpose is to query the configured
cloud service.
