import pytest
import os
import time
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from Automatyzacja.api_requests.generate_link import SendRequest
from pytest_metadata.plugin import metadata_key
driver = None


# Funkcja, która po przyjęciu argumentu --browser wybiera odpowiedni w zaleznosci od odpowiedzi
@pytest.fixture(autouse=True)
def setup(request, browser, url):
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome()  # Nie można zainstalować aktualnej wersji Chromedriver przez bank
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        driver = webdriver.Chrome()

    driver.get(SendRequest().get_fieldinfos())
    request.cls.driver = driver
    driver.maximize_window()

    yield
    driver.close()


# Obsługa konsoli i przyjęcie w niej argumentów po flagach --browser i --url
def pytest_addoption(parser):
    parser.addoption("--browser", action="store_true", default='chrome', help="specify which browser you want to use")
    parser.addoption("--url", action="store_true", default=False, help="specify url address")


# Obsługa flagi --browser
@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


# Obsługa flagi --url
@pytest.fixture(scope="class", autouse=True)
def url(request):
    return request.config.getoption("--url")


# Tytuł raportu
def pytest_html_report_title(report):
    report.title = "Automatyzacja spingo"


# Hookup tworzący raport
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    global driver
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # Zawsze dodaje url do end-point
        extra.append(pytest_html.extras.url(SendRequest().get_fieldinfos()))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # dodawaj dodatkowy html tylko po fail
            report_directory = os.path.dirname(item.config.option.htmlpath)
            file_name = str(int(round(time.time() * 1000))) + ".png"
            destinationfile = os.path.join(report_directory, file_name)
            # save_screenshot jest obsługiwany przez global driver, dlatego wyświetla błąd
            driver.save_screenshot(destinationfile)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:300px;height=200px" ' \
                       'onclick="window.open(this.src)" align="right"/></div>'%file_name
            extra.append(pytest_html.extras.html(html))
        report.extra = extra



