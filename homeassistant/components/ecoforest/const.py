"""Constants for the ecoforest integration."""

DOMAIN = "ecoforest"

# API
TIMEOUT = 10
INDOOR_TEMPERATURE = {
    "endpoint": "recepcion_datos_4.cgi",
    "payload": {"idOperacion": 1020},
    "var_name": "Ta",
}
WATER_PRESSURE = {
    "endpoint": "recepcion_datos_4.cgi",
    "payload": {"idOperacion": 1020},
    "var_name": "Pa",
}
POWER_LEVEL = {
    "endpoint": "recepcion_datos_4.cgi",
    "payload": {"idOperacion": 1020},
    "var_name": "Ni",
}
PUMP_SPEED = {
    "endpoint": "recepcion_datos_4.cgi",
    "payload": {"idOperacion": 1020},
    "var_name": "Co",
}
SMOKE_TEMPERATURE = {
    "endpoint": "recepcion_datos_4.cgi",
    "payload": {"idOperacion": 1020},
    "var_name": "Th",
}
FEED_RATE = {
    "endpoint": "recepcion_datos_4.cgi",
    "payload": {"idOperacion": 1020},
    "var_name": "Pn",
}
FORWARD_TEMPERATURE = {
    "endpoint": "recepcion_datos_4.cgi",
    "payload": {"idOperacion": 1020},
    "var_name": "Tn",
}
RETURN_TEMPERATURE = {
    "endpoint": "recepcion_datos_4.cgi",
    "payload": {"idOperacion": 1020},
    "var_name": "Rt",
}
