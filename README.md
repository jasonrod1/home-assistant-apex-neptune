# Home Assistant Apex Monitor

This custom integration pulls real-time probe data from a Neptune Apex system and makes it available in Home Assistant as sensors.

## Features
- Supports Temp, pH, ORP, Alk, Ca, Mg probes
- Parses local status.xml from Apex Controller
- Works offline / local network
- Designed for HACS install

## Installation
1. Add this repo as a [custom repository in HACS](https://hacs.xyz/)
2. Category: **Integration**
3. Install and restart Home Assistant

## Configuration
```yaml
sensor:
  - platform: apex_monitor
    url: "http://192.168.1.235/cgi-bin/status.xml"
```

## Coming Soon
- Auto-discovery via UI config flow
- LLM integration for reef trend summaries
- Coral health prediction using image+sensor data

MIT License | Created by @jasonrod1
