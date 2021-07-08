from selenium.webdriver.common.by import By

from infra.pages.abtract_page import AbstractPage
from infra.pages.home_page import HomePage
from infra.web.element_locator import ElementLocator


class LoginPage(AbstractPage):

    open_login_box_button = ElementLocator(By.LINK_TEXT, "Sign in")
    username_input = ElementLocator(By.ID, "username-pulldown")
    password_input = ElementLocator(By.ID, "password-pulldown")
    sign_in_button = ElementLocator(By.ID, "login-pulldown")

    def __init__(self, driver):
        super().__init__(driver)

    def write_username(self, username):
        self.wrapper_driver.click(self.open_login_box_button)
        self.wrapper_driver.send_keys(self.username_input, username)

    def write_password(self, password):
        self.wrapper_driver.send_keys(self.password_input, password)

    def click_on_sign_in_button(self) -> HomePage:
        self.wrapper_driver.click(self.sign_in_button)

        return HomePage(self.driver)
