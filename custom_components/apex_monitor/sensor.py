import requests
import xml.etree.ElementTree as ET
from homeassistant.helpers.entity import Entity
from .const import SENSOR_MAP

def setup_platform(hass, config, add_entities, discovery_info=None):
    apex_url = config.get("url", "http://192.168.1.235/cgi-bin/status.xml")
    sensors = [ApexSensor(apex_url, probe, *info) for probe, info in SENSOR_MAP.items()]
    add_entities(sensors, True)

class ApexSensor(Entity):
    def __init__(self, url, probe_name, friendly_name, unit):
        self._url = url
        self._probe = probe_name
        self._name = friendly_name
        self._unit = unit
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    def update(self):
        try:
            r = requests.get(self._url, timeout=10)
            root = ET.fromstring(r.content)
            for probe in root.findall(".//probe"):
                if probe.find("name").text.strip() == self._probe:
                    self._state = float(probe.find("value").text.strip())
        except Exception:
            self._state = None
