import pytest
import os
from utils.driver_factory import create_driver


@pytest.fixture
def setup():
    driver = create_driver()
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report= outcome.get_result()
    if report.when == 'call' and report.failed:
        driver = item.funcargs.get("setup")
        if driver:
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_file = os.path.join(screenshot_dir, f"{item.name}.png")  
            driver.save_screenshot(screenshot_file)


            