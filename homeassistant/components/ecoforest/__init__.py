"""The ecoforest integration."""
from __future__ import annotations

import requests

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

from .const import DOMAIN

# For your initial PR, limit it to 1 platform.
PLATFORMS: list[Platform] = [Platform.SENSOR]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up ecoforest from a config entry."""

    hass.data.setdefault(DOMAIN, {})

    _session = requests.Session()
    _host = entry.data["host"]
    _session.auth = (entry.data["username"], entry.data["password"])

    _auth_response = await hass.async_add_executor_job(
        lambda: _session.get(_host, verify=False)
    )

    if _auth_response.status_code == 200:

        hass.data[DOMAIN]["api"] = {"session": _session, "host": _host}

        await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

        return True

    return False


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    if unload_ok := await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok
