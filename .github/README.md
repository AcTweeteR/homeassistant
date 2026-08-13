# Repository automation

The files in this directory maintain project quality and support:

- `workflows/validate.yml`: runs Hassfest and HACS validation;
- `workflows/lint.yml`: checks Python style with Ruff;
- `workflows/release.yml`: packages Livoltek and attaches its ZIP to releases;
- `ISSUE_TEMPLATE/`: collects reproducible bug reports and feature requests.

Issue templates remind contributors to remove credentials and private data.

This workflow set belongs only to the Livoltek integration. Each future
integration will have its own repository and independent validation history.
