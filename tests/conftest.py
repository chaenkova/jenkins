import pytest
from selene import browser
from selenium import webdriver

from helpers import attach
import os

from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="function",autouse=True)
def browser_settings():
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.config.base_url = 'https://demoqa.com'

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    selenoid_url = os.getenv("SELENOID_URL")

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
        options=options)

    browser.config.driver = driver

    yield
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()
