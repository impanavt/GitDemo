import pytest
from selenium import webdriver
import time
driver=None
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import os
from pytest import *
import requests

# to do browser invocation like chrome firfox you need to use command line so that --browser_name can be used at cli
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome")


@pytest.fixture(scope='class')
def setup(request):
    # when defined global as driver it will use the driver initially defined so all drivers defined use global one
    global driver
    # to retrieve value from browser
    browser_name = request.config.getoption("browser_name")
    if browser_name == 'chrome':
        driver = webdriver.Chrome()
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.maximize_window()
        # driver.find_element(By.CSS_SELECTOR, ".card-title a")

    # we are assigning local driver of fixture  to class  driver whichever class uses that fixture if it has class
    # variable
    elif browser_name == 'firefox':
        driver = webdriver.Firefox()
        request.cls.driver = driver
        # to return driver after yield assigning local driver of fixture to class driver
        # yield

        # driver.close()
    yield driver

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
        """
            Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
            :param item:
            """
        pytest_html = item.config.pluginmanager.getplugin('html')
        outcome = yield
        report = outcome.get_result()
        extra = getattr(report, 'extra', [])

        if report.when == 'call' or report.when == "setup":
            xfail = hasattr(report, 'wasxfail')
            if (report.skipped and xfail) or (report.failed and not xfail):
                file_name = report.nodeid.replace("::", "_") + ".png"
                _capture_screenshot(file_name)
                # screenshot will come and form as htmp report
                if file_name:
                    html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                           'onclick="window.open(this.src)" align="right"/></div>' % file_name
                    extra.append(pytest_html.extras.html(html))
            report.extra = extra

def _capture_screenshot(name):
     driver.get_screenshot_as_file(name)


