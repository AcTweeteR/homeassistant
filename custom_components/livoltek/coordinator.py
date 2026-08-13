"""DataUpdateCoordinator for the Livoltek integration."""
from __future__ import annotations

import datetime as dt
from typing import Any

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from .const import (
    CONF_SITE_ID,
    CONF_USERTOKEN_ID,
    DOMAIN,
    LOGGER,
    SCAN_INTERVAL,
)
from .helper import (
    async_get_api_client,
    async_get_cur_power_flow,
    async_get_device_list,
    async_get_recent_grid,
    async_get_recent_solar,
    async_get_site,
)


class LivoltekDataUpdateCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    """The Livoltek Data Update Coordinator."""

    config_entry: ConfigEntry
    hass: HomeAssistant
    access_token: str | None = None

    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None:
        """Initialize the Livoltek coordinator."""
        self.config_entry = entry
        self.hass = hass

        self.site = None
        self.devices: list = []
        self.current_power_flow = None
        self.todays_grid = None
        self.todays_solar = None
        self._empty_device_list_count: int = 0

        super().__init__(hass, LOGGER, name=DOMAIN, update_interval=SCAN_INTERVAL)

    async def _async_update_data(self) -> dict[str, Any]:
        """Fetch system status from Livoltek."""
        # Keep last known values as fallback; only reset if we get fresh data
        new_grid = None
        new_solar = None

        try:
            api, self.access_token = await async_get_api_client(
                self.config_entry,
                self.access_token,
            )

            user_token = self.config_entry.data[CONF_USERTOKEN_ID]
            site_id = self.config_entry.data[CONF_SITE_ID]

            site = await async_get_site(api, user_token, site_id)
            devices = await async_get_device_list(api, user_token, site_id)
            current_power_flow = await async_get_cur_power_flow(api, user_token, site_id)
            recent_grid = await async_get_recent_grid(api, user_token, site_id)
            recent_solar = await async_get_recent_solar(api, user_token, site_id)

        except Exception as err:
            raise UpdateFailed(f"Error communicating with Livoltek API: {err}") from err

        today = dt.date.today()

        if recent_grid:
            for grid in recent_grid:
                try:
                    ts = dt.date.fromtimestamp(int(grid["ts"]) / 1000)
                    if ts == today and (
                        new_grid is None
                        or int(grid["ts"]) > int(new_grid["ts"])
                    ):
                        new_grid = grid
                except (KeyError, TypeError, ValueError) as err:
                    LOGGER.debug("Skipping invalid Livoltek grid item %s: %s", grid, err)

        if recent_solar:
            for solar in recent_solar:
                try:
                    ts = dt.date.fromtimestamp(int(solar["ts"]) / 1000)
                    if ts == today and (
                        new_solar is None
                        or int(solar["ts"]) > int(new_solar["ts"])
                    ):
                        new_solar = solar
                except (KeyError, TypeError, ValueError) as err:
                    LOGGER.debug("Skipping invalid Livoltek solar item %s: %s", solar, err)

        # Only update stored values if fresh data was obtained; otherwise keep last known
        if new_grid is not None:
            self.todays_grid = new_grid
        if new_solar is not None:
            self.todays_solar = new_solar

        self.site = site

        # devices is a plain list of dicts returned by async_get_device_list.
        # Only overwrite if we got a non-empty list to preserve last known state.
        # If the list is empty for several consecutive cycles, force a token refresh:
        # the API silently returns an empty list when the token expires instead of
        # returning an HTTP error, so we would otherwise loop forever without recovery.
        if devices:
            self.devices = devices
            self._empty_device_list_count = 0
        else:
            self._empty_device_list_count += 1
            LOGGER.warning(
                "Livoltek API returned empty device list, keeping previous state "
                "(consecutive count: %d)",
                self._empty_device_list_count,
            )
            if self._empty_device_list_count >= 3:
                LOGGER.warning(
                    "Livoltek: forcing token refresh after %d consecutive empty "
                    "device lists (token may have expired silently)",
                    self._empty_device_list_count,
                )
                self.access_token = None
                self._empty_device_list_count = 0

        if current_power_flow is not None:
            try:
                self.current_power_flow = current_power_flow.data
                LOGGER.debug("Current Power Flow: %s", self.current_power_flow)
            except (IndexError, AttributeError, TypeError) as err:
                LOGGER.warning("Invalid Livoltek current power flow response: %s", err)
                self.current_power_flow = None
        else:
            # None is normal outside daylight hours; debug level avoids log noise
            LOGGER.debug("Livoltek current power flow unavailable (likely nighttime or offline)")

        return {
            "site": self.site,
            "devices": self.devices,
            "current_power_flow": self.current_power_flow,
            "todays_grid": self.todays_grid,
            "todays_solar": self.todays_solar,
        }
