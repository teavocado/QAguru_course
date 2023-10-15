import pytest
from selene import browser


@pytest.fixture
def test_open_browser( ):
    browser.open("https://www.google.com/")
