import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="edge", help="browser selection"
    )
options = Options()
options.add_argument("--incognito")

@pytest.fixture(scope="function")
def browser_instance(request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    elif browser_name == "edge":
        driver = webdriver.Edge(service=Service("/usr/local/bin/msedgedriver"))
    elif browser_name == "safari":
        driver = webdriver.Safari()
    else:
        raise ValueError(f"Browser {browser_name} is not supported")
    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    yield driver
    driver.quit()
