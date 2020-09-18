""" Test Mail and Packages Sensor """
import datetime
import email
from custom_components.mail_and_packages.const import DOMAIN

from pytest_homeassistant_custom_component.common import MockConfigEntry


async def setup_mnp(hass):
    entry = MockConfigEntry(
        domain=DOMAIN,
        title="imap.test.email",
        data={
            "amazon_fwds": '""',
            "folder": '"INBOX"',
            "generate_mp4": false,
            "gif_duration": 5,
            "host": "imap.test.email",
            "image_path": "/config/www/mail_and_packages/",
            "image_security": true,
            "password": "suchfakemuchpassword",
            "port": 993,
            "resources": [
                "amazon_packages",
                "fedex_delivered",
                "fedex_delivering",
                "fedex_packages",
                "mail_updated",
                "ups_delivered",
                "ups_delivering",
                "ups_packages",
                "usps_delivered",
                "usps_delivering",
                "usps_mail",
                "usps_packages",
                "zpackages_delivered",
                "zpackages_transit",
                "dhl_delivered",
                "dhl_delivering",
                "dhl_packages",
                "amazon_delivered",
            ],
            "scan_interval": 20,
            "username": "user@fake.email",
        },
    )

    entry.add_to_hass(hass)
    await hass.config_entries.async_setup(entry.entry_id)
    await hass.async_block_till_done()


async def test_sensor(hass):
    await setup_mnp(hass)

    test_message = email.message.Message()
    test_message["From"] = "sender@test.com"
    test_message["Subject"] = "Test"
    test_message["Date"] = datetime.datetime.now()
    test_message.set_payload("Test Message")
