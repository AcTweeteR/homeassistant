# Installation

## Install Livoltek with HACS

Livoltek is a custom Home Assistant integration, not an add-on. HACS installs
its files under `custom_components/livoltek/`.

### Recommended installation

[![Open in HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=AcTweeteR&repository=homeassistant&category=integration)

1. Open the button above or go to **HACS > Integrations**.
2. Search for **Livoltek**.
3. Select **Download** and restart Home Assistant if requested.
4. Go to **Settings > Devices & services > Add integration**.
5. Search for **Livoltek** and complete the form.

### Custom repository installation

If Livoltek is not yet listed in the HACS catalog:

1. Open **HACS > Integrations > three-dot menu > Custom repositories**.
2. Add `https://github.com/AcTweeteR/homeassistant`.
3. Select category **Integration**.
4. Install Livoltek and restart Home Assistant.

## Home Assistant add-on store

This repository is intentionally not published as an add-on repository. The
Livoltek project is an integration and will not appear in the add-on store. If
a real add-on is added under `addons/` in the future, repository metadata and
separate installation instructions will be published at that time.
