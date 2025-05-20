import pytest
import os
from utils.driver_factory import create_driver
import webbrowser
from pathlib import Path


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

def pytest_sessionfinish(session, exitstatus):
    """Hook to open HTML report automatically after tests finish"""
    report_path = Path("reports/test_report.html").resolve()
    if report_path.exists():
        webbrowser.open_new_tab(f"file://{report_path}")

            