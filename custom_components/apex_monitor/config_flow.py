from homeassistant import config_entries
import voluptuous as vol
from homeassistant.core import callback
from .const import DOMAIN

DATA_SCHEMA = vol.Schema({
    vol.Required("ip_address"): str,
    vol.Optional("username", default="admin"): str,
    vol.Optional("password"): str,
})

class ApexMonitorConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            return self.async_create_entry(
                title=f"Apex @ {user_input['ip_address']}",
                data=user_input
            )

        return self.async_show_form(
            step_i_
