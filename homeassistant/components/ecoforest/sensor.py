"""Platform for sensor integration."""
from __future__ import annotations

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import PERCENTAGE, PRESSURE_BAR, TEMP_CELSIUS, TIME_SECONDS
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import (
    DOMAIN,
    FEED_RATE,
    FORWARD_TEMPERATURE,
    INDOOR_TEMPERATURE,
    POWER_LEVEL,
    PUMP_SPEED,
    RETURN_TEMPERATURE,
    SMOKE_TEMPERATURE,
    WATER_PRESSURE,
)


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up entry."""
    # coordinator = hass.data[DOMAIN][config_entry.entry_id]
    # channels = coordinator.data.channels
    # entities: list[EmonitorPowerSensor] = []
    # seen_channels = set()

    async_add_entities(
        [
            IndoorTemperature(),
            WaterPressure(),
            PowerLevel(),
            PumpSpeed(),
            SmokeTemperature(),
            FeedRate(),
            ForwardTemperature(),
            ReturnTemperature(),
        ]
    )


def payload_deserializer(payload: str) -> dict:
    """Payload handler."""

    data_expanded = [measure.strip().split(sep="=") for measure in payload.split("\n")]
    data_expanded.pop(-1)
    out: dict = {row[0]: row[1] for row in data_expanded}

    return out


class IndoorTemperature(SensorEntity):
    """Representation of a Sensor."""

    _attr_name = "Indoor Temperature"
    _attr_native_unit_of_measurement = TEMP_CELSIUS
    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_state_class = SensorStateClass.MEASUREMENT

    def update(self) -> None:
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """

        _host = self.hass.data[DOMAIN]["api"]["host"]

        _session = self.hass.data[DOMAIN]["api"]["session"]

        result = _session.post(
            f"{_host}/{INDOOR_TEMPERATURE['endpoint']}", INDOOR_TEMPERATURE["payload"]
        )

        payload: dict = payload_deserializer(result.text)

        self._attr_native_value = float(payload[INDOOR_TEMPERATURE["var_name"]])


class WaterPressure(SensorEntity):
    """Representation of a Sensor."""

    _attr_name = "Water Pressure"
    _attr_native_unit_of_measurement = PRESSURE_BAR
    _attr_device_class = SensorDeviceClass.PRESSURE
    _attr_state_class = SensorStateClass.MEASUREMENT

    def update(self) -> None:
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """

        _host = self.hass.data[DOMAIN]["api"]["host"]

        _session = self.hass.data[DOMAIN]["api"]["session"]

        result = _session.post(
            f"{_host}/{WATER_PRESSURE['endpoint']}", WATER_PRESSURE["payload"]
        )

        payload: dict = payload_deserializer(result.text)

        self._attr_native_value = float(payload[WATER_PRESSURE["var_name"]])


class PowerLevel(SensorEntity):
    """Representation of a Sensor."""

    _attr_name = "Power Level"
    _attr_native_unit_of_measurement = ""
    _attr_device_class = SensorDeviceClass.POWER
    _attr_state_class = SensorStateClass.MEASUREMENT

    def update(self) -> None:
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """

        _host = self.hass.data[DOMAIN]["api"]["host"]

        _session = self.hass.data[DOMAIN]["api"]["session"]

        result = _session.post(
            f"{_host}/{POWER_LEVEL['endpoint']}", POWER_LEVEL["payload"]
        )

        payload: dict = payload_deserializer(result.text)

        self._attr_native_value = int(payload[POWER_LEVEL["var_name"]])


class PumpSpeed(SensorEntity):
    """Representation of a Sensor."""

    _attr_name = "Pump Speed"
    _attr_native_unit_of_measurement = PERCENTAGE
    _attr_device_class = SensorDeviceClass.SPEED
    _attr_state_class = SensorStateClass.MEASUREMENT

    def update(self) -> None:
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """

        _host = self.hass.data[DOMAIN]["api"]["host"]

        _session = self.hass.data[DOMAIN]["api"]["session"]

        result = _session.post(
            f"{_host}/{PUMP_SPEED['endpoint']}", PUMP_SPEED["payload"]
        )

        payload: dict = payload_deserializer(result.text)

        self._attr_native_value = float(payload[PUMP_SPEED["var_name"]])


class SmokeTemperature(SensorEntity):
    """Representation of a Sensor."""

    _attr_name = "Smoke Temperature"
    _attr_native_unit_of_measurement = TEMP_CELSIUS
    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_state_class = SensorStateClass.MEASUREMENT

    def update(self) -> None:
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """

        _host = self.hass.data[DOMAIN]["api"]["host"]

        _session = self.hass.data[DOMAIN]["api"]["session"]

        result = _session.post(
            f"{_host}/{SMOKE_TEMPERATURE['endpoint']}", SMOKE_TEMPERATURE["payload"]
        )

        payload: dict = payload_deserializer(result.text)

        self._attr_native_value = float(payload[SMOKE_TEMPERATURE["var_name"]])


class FeedRate(SensorEntity):
    """Representation of a Sensor."""

    _attr_name = "Feed Rate"
    _attr_native_unit_of_measurement = TIME_SECONDS
    _attr_device_class = SensorDeviceClass.DURATION
    _attr_state_class = SensorStateClass.MEASUREMENT

    def update(self) -> None:
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """

        _host = self.hass.data[DOMAIN]["api"]["host"]

        _session = self.hass.data[DOMAIN]["api"]["session"]

        result = _session.post(f"{_host}/{FEED_RATE['endpoint']}", FEED_RATE["payload"])

        payload: dict = payload_deserializer(result.text)

        self._attr_native_value = float(payload[FEED_RATE["var_name"]])


class ForwardTemperature(SensorEntity):
    """Representation of a Sensor."""

    _attr_name = "Forward Temperature"
    _attr_native_unit_of_measurement = TEMP_CELSIUS
    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_state_class = SensorStateClass.MEASUREMENT

    def update(self) -> None:
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """

        _host = self.hass.data[DOMAIN]["api"]["host"]

        _session = self.hass.data[DOMAIN]["api"]["session"]

        result = _session.post(
            f"{_host}/{FORWARD_TEMPERATURE['endpoint']}", FORWARD_TEMPERATURE["payload"]
        )

        payload: dict = payload_deserializer(result.text)

        self._attr_native_value = float(payload[FORWARD_TEMPERATURE["var_name"]])


class ReturnTemperature(SensorEntity):
    """Representation of a Sensor."""

    _attr_name = "Return Temperature"
    _attr_native_unit_of_measurement = TEMP_CELSIUS
    _attr_device_class = SensorDeviceClass.TEMPERATURE
    _attr_state_class = SensorStateClass.MEASUREMENT

    def update(self) -> None:
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """

        _host = self.hass.data[DOMAIN]["api"]["host"]

        _session = self.hass.data[DOMAIN]["api"]["session"]

        result = _session.post(
            f"{_host}/{RETURN_TEMPERATURE['endpoint']}", RETURN_TEMPERATURE["payload"]
        )

        payload: dict = payload_deserializer(result.text)

        self._attr_native_value = float(payload[RETURN_TEMPERATURE["var_name"]])
