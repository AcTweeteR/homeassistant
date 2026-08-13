"""Livoltek API helpers."""
from __future__ import annotations

import asyncio
from typing import Any

import jwt as _pyjwt
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_API_KEY
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.device_registry import DeviceInfo
from pylivoltek import ApiClient, ApiLoginBody, Configuration
from pylivoltek.api import DefaultApi
from pylivoltek.models import (
    CurrentPowerFlow,
    DeviceDetails,
    DeviceList,
    GridImportExportList,
    Site,
    SolarGenerationtList,
)
from pylivoltek.rest import ApiException

from .const import (
    CONF_EMEA_ID,
    CONF_SECUID_ID,
    CONF_SITE_ID,
    CONF_USERTOKEN_ID,
    DOMAIN,
    LIVOLTEK_EMEA_SERVER,
    LIVOLTEK_GLOBAL_SERVER,
    LOGGER,
)

API_TIMEOUT = 30


def validate_jwt(token: str | None) -> bool:
    """Validate a JWT token header without verifying the signature."""
    if not token or not isinstance(token, str):
        return False

    try:
        _pyjwt.get_unverified_header(token)
    except Exception as err:
        LOGGER.info("Invalid JWT token: %s", err)
        return False

    return True


async def async_get_login_token(host: str, api_key: str, secuid: str) -> str:
    """Get the login token for the Livoltek API."""
    config = Configuration()
    config.host = host

    api_key = api_key.replace("\\r", "\r").replace("\\n", "\n")

    api_client = ApiClient(config)
    model = ApiLoginBody(secuid, api_key)
    api = DefaultApi(api_client)

    try:
        async with asyncio.timeout(API_TIMEOUT):
            thread = api.hess_api_login_post_with_http_info(
                model,
                async_req=True,
                _preload_content=True,
            )
            thread_result = thread.get(timeout=API_TIMEOUT)
    except (TimeoutError, asyncio.TimeoutError) as err:
        raise ConfigEntryAuthFailed(
            f"Login timeout after {API_TIMEOUT}s: {err}"
        ) from err
    except ApiException as err:
        raise ConfigEntryAuthFailed(f"Login API error: {err}") from err

    response = thread_result[0]

    if getattr(response, "message", None) != "SUCCESS":
        raise ConfigEntryAuthFailed(getattr(response, "message", "Login failed"))

    data = getattr(response, "data", None)
    if not data or "data" not in data:
        raise ConfigEntryAuthFailed("Login response did not contain an access token")

    return data["data"]


async def async_get_api_client(
    entry: ConfigEntry,
    access_token: str | None = None,
) -> tuple[DefaultApi, str]:
    """Get the Livoltek API client."""
    config = Configuration()

    emea = bool(entry.data[CONF_EMEA_ID])
    secuid = str(entry.data[CONF_SECUID_ID])
    api_key = str(entry.data[CONF_API_KEY])

    config.host = LIVOLTEK_EMEA_SERVER if emea else LIVOLTEK_GLOBAL_SERVER

    if validate_jwt(access_token):
        token = access_token
    else:
        LOGGER.info("Livoltek access token is invalid or missing, refreshing")
        token = await async_get_login_token(config.host, api_key, secuid)

    api_client = ApiClient(config)
    api_client.set_default_header("Authorization", token)
    return DefaultApi(api_client), token


async def async_get_site(
    api: DefaultApi,
    user_token: str,
    site_id: str,
) -> Site | None:
    """Get the Livoltek site overview."""
    try:
        async with asyncio.timeout(API_TIMEOUT):
            thread = api.hess_api_site_site_id_overview_get_with_http_info(
                user_token,
                site_id,
                async_req=True,
            )
            # [0] extracts the response object from the (response, status, headers) tuple
            return thread.get(timeout=API_TIMEOUT)[0]
    except (TimeoutError, asyncio.TimeoutError):
        LOGGER.warning("Livoltek site overview timed out after %ss", API_TIMEOUT)
    except Exception as err:
        LOGGER.error("Error getting Livoltek site overview: %s", err)

    return None


async def async_get_cur_power_flow(
    api: DefaultApi,
    user_token: str,
    site_id: str,
) -> CurrentPowerFlow | None:
    """Get the current power flow."""
    try:
        async with asyncio.timeout(API_TIMEOUT):
            thread = api.hess_api_site_site_id_cur_powerflow_get_with_http_info(
                user_token,
                site_id,
                async_req=True,
            )
            # [0] extracts the response object from the (response, status, headers) tuple
            return thread.get(timeout=API_TIMEOUT)[0]
    except (TimeoutError, asyncio.TimeoutError):
        LOGGER.warning("Livoltek power flow timed out after %ss", API_TIMEOUT)
    except ApiException as err:
        LOGGER.error("Error getting Livoltek current power flow: %s", err)
    except Exception as err:
        LOGGER.error("Unexpected error getting Livoltek current power flow: %s", err)

    return None


async def async_get_device_list(
    api: DefaultApi,
    user_token: str,
    site_id: str,
) -> list[dict[str, Any]]:
    """Get the Livoltek device list."""
    try:
        async with asyncio.timeout(API_TIMEOUT):
            thread = api.hess_api_device_site_id_list_get_with_http_info(
                user_token,
                site_id,
                1,
                10,
                async_req=True,
            )
            device_list = thread.get(timeout=API_TIMEOUT)
    except (TimeoutError, asyncio.TimeoutError):
        LOGGER.warning("Livoltek device list timed out after %ss", API_TIMEOUT)
        return []
    except Exception as err:
        LOGGER.error("Error getting Livoltek device list: %s", err)
        return []

    try:
        raw_data = device_list[0].data
    except (IndexError, AttributeError, TypeError) as err:
        LOGGER.warning("Invalid Livoltek device list response: %s", err)
        return []

    if not raw_data:
        LOGGER.warning("Livoltek API returned empty device list, skipping update")
        return []

    # raw_data may be a dict or a pydantic/dataclass object; normalise to dict access
    if isinstance(raw_data, dict):
        return raw_data.get("list", [])

    # Object with attribute access (pydantic model)
    device_entries = getattr(raw_data, "list", None)
    if device_entries is None:
        LOGGER.warning("Livoltek device list has no 'list' attribute: %s", type(raw_data))
        return []

    return device_entries


async def async_get_device_generation(
    api: DefaultApi,
    user_token: str,
    device_id: str,
) -> DeviceList | None:
    """Get device generation data."""
    try:
        async with asyncio.timeout(API_TIMEOUT):
            thread = api.hess_api_device_device_id_real_electricity_get_with_http_info(
                user_token,
                device_id,
                async_req=True,
            )
            device_generation = thread.get(timeout=API_TIMEOUT)
            return device_generation[0]
    except (TimeoutError, asyncio.TimeoutError):
        LOGGER.warning("Livoltek device generation timed out after %ss", API_TIMEOUT)
    except Exception as err:
        LOGGER.error("Error getting Livoltek device generation: %s", err)

    return None


async def async_get_recent_grid(
    api: DefaultApi,
    user_token: str,
    site_id: str,
) -> list[dict[str, Any]] | None:
    """Get the recent grid import/export data."""
    try:
        async with asyncio.timeout(API_TIMEOUT):
            thread = api.get_recent_energy_import_export_with_http_info(
                user_token,
                site_id,
                async_req=True,
            )
            recent_grid = thread.get(timeout=API_TIMEOUT)
    except (TimeoutError, asyncio.TimeoutError):
        LOGGER.warning("Livoltek recent grid timed out after %ss", API_TIMEOUT)
        return None
    except Exception as err:
        LOGGER.error("Error getting Livoltek recent grid: %s", err)
        return None

    # recent_grid is a (response, status, headers) tuple; extract the response object
    try:
        response_obj = recent_grid[0]
    except (IndexError, TypeError) as err:
        LOGGER.warning("Unexpected Livoltek recent grid response structure: %s", err)
        return None

    # The response object may be a dict or a model; extract 'data' safely in both cases
    if isinstance(response_obj, dict):
        data = response_obj.get("data")
    else:
        data = getattr(response_obj, "data", None)

    if data is None:
        LOGGER.debug("Livoltek recent grid response contains no 'data' field (API may be rate-limiting or inverter offline)")
        return None

    return data


async def async_get_recent_solar(
    api: DefaultApi,
    user_token: str,
    site_id: str,
) -> list[dict[str, Any]] | None:
    """Get the recent solar generation data."""
    try:
        async with asyncio.timeout(API_TIMEOUT):
            thread = api.get_recent_solar_generated_energy_with_http_info(
                user_token,
                site_id,
                async_req=True,
            )
            recent_solar = thread.get(timeout=API_TIMEOUT)
    except (TimeoutError, asyncio.TimeoutError):
        LOGGER.warning("Livoltek recent solar timed out after %ss", API_TIMEOUT)
        return None
    except Exception as err:
        LOGGER.error("Error getting Livoltek recent solar: %s", err)
        return None

    # recent_solar is a (response, status, headers) tuple; extract the response object
    try:
        response_obj = recent_solar[0]
    except (IndexError, TypeError) as err:
        LOGGER.warning("Unexpected Livoltek recent solar response structure: %s", err)
        return None

    # The response object may be a dict or a model; extract 'data' safely in both cases
    if isinstance(response_obj, dict):
        data = response_obj.get("data")
    else:
        data = getattr(response_obj, "data", None)

    if data is None:
        LOGGER.debug("Livoltek recent solar response contains no 'data' field (API may be rate-limiting or inverter offline)")
        return None

    return data


async def async_update_devices(entry: ConfigEntry, hass: HomeAssistant) -> None:
    """Update Livoltek devices."""
    api, _token = await async_get_api_client(entry)
    user_token = str(entry.data[CONF_USERTOKEN_ID])
    site_id = str(entry.data[CONF_SITE_ID])

    device_list = await async_get_device_list(api, user_token, site_id)
    await async_register_devices(api, entry, user_token, site_id, device_list, hass)


async def async_register_devices(
    api: DefaultApi,
    entry: ConfigEntry,
    user_token: str,
    site_id: str,
    device_list: list[dict[str, Any]],
    hass: HomeAssistant,
) -> None:
    """Register Livoltek devices."""
    device_registry = dr.async_get(hass)

    for device in device_list:
        inverter_sn = device.get("inverterSn")
        if not inverter_sn:
            LOGGER.debug("Skipping Livoltek device without inverterSn: %s", device)
            continue

        try:
            async with asyncio.timeout(10):
                thread = api.get_device_details(
                    user_token,
                    site_id,
                    inverter_sn,
                    async_req=True,
                    _preload_content=True,
                )
                dev = thread.get(timeout=10).data
        except Exception as err:
            LOGGER.warning("Could not register Livoltek device %s: %s", inverter_sn, err)
            continue

        device_registry.async_get_or_create(
            config_entry_id=entry.entry_id,
            identifiers={(DOMAIN, dev.id)},
            manufacturer=dev.device_manufacturer,
            name=dev.inverter_sn,
            model=dev.product_type,
            serial_number=dev.inverter_sn,
            sw_version=dev.firmware_version,
        )


async def async_get_hass_device_info(
    entry: ConfigEntry,
    device: DeviceDetails,
) -> DeviceInfo:
    """Get device info for Home Assistant."""
    return DeviceInfo(
        identifiers={(DOMAIN, device.id)},
        manufacturer=device.device_manufacturer,
        name=device.inverter_sn,
        model=device.product_type,
        sw_version=device.firmware_version,
        serial_number=device.inverter_sn,
    )
