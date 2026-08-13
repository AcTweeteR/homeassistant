# Home Assistant OS add-ons

This directory is reserved for future real add-ons maintained in this
repository. It is not currently part of Livoltek's HACS distribution and this
repository is not published to the Home Assistant add-on store.

Each future add-on must have its own directory, for example
`addons/my_addon/`, containing at least:

- `config.yaml` with official add-on metadata;
- a `Dockerfile` or a valid container image reference;
- a `README.md` covering installation, configuration, permissions and support;
- every file required to build and run the add-on.

Do not store backups, build output or temporary directories under `addons/`.
