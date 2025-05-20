from selenium import webdriver

def create_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")  # prevents user-data-dir conflicts
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    return driver

