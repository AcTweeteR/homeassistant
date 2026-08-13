# Development scripts

This directory contains utilities inherited from the integration development
environment:

- `setup`: prepares the local virtual environment and dependencies;
- `develop`: starts the development Home Assistant instance;
- `lint`: runs style checks;
- `rebuild.sh`: rebuilds the development environment after dependency changes;
- `cli-gen.sh` and `cli-gen-opts.json`: API-client generation support;
- `pip_packages`: reference package list for the development environment.

These scripts are development tools and are not used by HACS at runtime.
