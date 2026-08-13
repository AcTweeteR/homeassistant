# Changelog

## 1.0.1

- Removed unused imports reported by Ruff.
- Added the repository topics required by HACS validation.

## 1.0.0

- Initial public AcTweeteR release of the maintained Livoltek adaptation.
- Updated Home Assistant config-flow typing and async API calls.
- Added defensive API timeouts and response validation.
- Preserved the last valid values when Livoltek returns no data temporarily.
- Added token refresh recovery after repeated empty device responses.
- Added daily grid and solar energy sensors.
- Added HACS and Home Assistant add-on repository instructions.
