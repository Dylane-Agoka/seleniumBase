from seleniumbase import BaseCase
BaseCase.main(__name__, __file__) # Call pytest

class MyTestClass(BaseCase):
    def test_swag_labs(self):
        self.open("https://www.saucedemo.com")
        self.type("#user-name", "standard_user")
        self.type("#password", "secret_sauce\n")
        self.assert_element("div.inventory_list")
        self.click('button[name*="backpack"]')
        self.click("#shopping_cart_container a")
        self.assert_text("Backpack", "div.cart_item")
        self.click("button#checkout")
        self.type("")