from pages.login_page import LoginPage
import time

def test_valid_login(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.load()
    time.sleep(2)
    login_page.login("standard_user", "secret_sauce")
    time.sleep(5)

    login_page.buy_backpack()
    time.sleep(5)

    login_page.check_info("Steve", "Smith", "2123")
    time.sleep(5)

    login_page.verify_item_details("Sauce Labs Backpack", "1", "32.39")
    time.sleep(5)

    login_page.click_finish()

    print(f"Current URL: " , {driver.current_url})

    assert "Thank you!" in driver.page_source
    print("✅ Assertion passed: 'Thank you!' found in page source.")
