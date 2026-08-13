# Development

## Repository layout

```text
custom_components/livoltek/  Home Assistant integration source and manifest
tests/                        Automated tests
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

## Repository boundaries

This repository is dedicated to the Livoltek integration. New integrations
should use their own repository so users can find and install them directly
from HACS without downloading unrelated projects.
