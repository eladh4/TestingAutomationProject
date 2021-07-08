from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from infra.pages.home_page import HomePage
from infra.pages.login_page import LoginPage
from infra.web.element_locator import ElementLocator
from main_config import config

driver: WebDriver = None


def login(username, password) -> HomePage:
    url = config["base_url"]

    global driver

    if driver is None:
        driver = webdriver.Chrome(executable_path="C:/Users/eladh/PycharmProjects/TestingAutomationProject/drivers/chromedriver.exe")
        driver.implicitly_wait(10)

    driver.get(url)
    driver.maximize_window()

    login_page = LoginPage(driver)

    login_page.write_username(username)
    login_page.write_password(password)

    home_page = login_page.click_on_sign_in_button()
    return home_page


def logout():
    driver.find_element_by_xpath('//a [@title="OpenProject Admin"]').click()
    driver.find_element_by_class_name("logout-menu-item").click()
