# Development

## Repository layout

```text
custom_components/livoltek/  Home Assistant integration source and manifest
tests/                        Automated tests
addons/                       Reserved for a future real add-on
docs/                         User, support and developer documentation
.github/workflows/            Validation, lint and release workflows
```

## Local validation

```bash
python3 -m ruff check .
pytest
```

Update the documentation and changelog before opening a pull request. Changes
to integration behavior should include focused tests whenever practical.

## Future add-ons

If a real add-on is ever published, create `addons/<slug>/config.yaml` and add
all files required to build and run it. At that point, publish the official
Home Assistant add-on repository metadata and separate installation guidance.
Do not place backups, build output or temporary directories under `addons/`.
