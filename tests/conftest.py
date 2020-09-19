""" Fixtures for Mail and Packages tests. """

from custom_components.mail_and_packages.tests.const import FAKE_UPDATE_DATA
import pytest

pytest_plugins = "pytest_homeassistant_custom_component"


@pytest.fixture(name="generic_data", scope="session")
def mock_generic_data():
    """ Mock email data update class values. """
    data = FAKE_UPDATE_DATA

    return data
