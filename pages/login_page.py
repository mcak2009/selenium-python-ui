from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.add_to_cart_backpack_field = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.shopping_cart = (By.ID, "shopping_cart_container")
        self.checkout = (By.ID, "checkout")
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.Continue = (By.ID, "continue")
        self.description = (By.CLASS_NAME, "inventory_item_name")
        self.quantity = (By.CLASS_NAME, "cart_quantity")
        self.total_price = (By.CLASS_NAME, "summary_total_label")
        self.finish_b = (By.ID, "finish")

        print("✅ Item description and quantity verified successfully.")


    def load(self):
        self.driver.get("https://www.saucedemo.com")

    def login(self, username, password):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def buy_backpack(self):
        self.driver.find_element(*self.add_to_cart_backpack_field).click()
        self.driver.find_element(*self.shopping_cart).click()
        self.driver.find_element(*self.checkout).click()

    def check_info(self, firstname, lastname, postalcode):
        self.driver.find_element(*self.first_name).send_keys(firstname)
        self.driver.find_element(*self.last_name).send_keys(lastname)
        self.driver.find_element(*self.postal_code).send_keys(postalcode)
        self.driver.find_element(*self.Continue).click()

    def verify_item_details(self, expected_description, expected_quantity, expected_total_price):
        actual_description = self.driver.find_element(*self.description).text
        actual_quantity = self.driver.find_element(*self.quantity).text
        actual_total_price = self.driver.find_element(*self.total_price).text


        assert expected_description in actual_description, f"Expected description '{expected_description}' not in '{actual_description}'"
        assert expected_quantity == actual_quantity, f"Expected quantity '{expected_quantity}', got '{actual_quantity}'"
        assert expected_total_price in actual_total_price, f"Expected total price '{expected_total_price}' not in '{actual_total_price}'"

    print("✅ Item description, quantity, and price verified successfully.")

    def click_finish(self):
        self.driver.find_element(*self.finish_b).click()



    



    


