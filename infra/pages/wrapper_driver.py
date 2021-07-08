from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class WrapperDriver():

    def __init__(self, driver):
        self.driver = driver

    def click(self, element_locator):
        element = self.get_element(element_locator)
        element.click()

    def send_keys(self, element_locator, text):
        element = self.get_element(element_locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, element_locator):
        element = self.get_element(element_locator, element_must_be_visible=False)
        return element.text

    def get_element(self, element_locator, element_must_be_visible: bool = True):
        if element_must_be_visible:
            return self.wait_for_visibility_of_element(element_locator)
        else:
            return self.wait_for_presence_of_element(element_locator)

    def get_elements(self, element_locator):
        elements = self.driver.find_elements(element_locator.by, element_locator.value)
        return elements

    def wait_for_visibility_of_element(self, element_locator):
        element = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((element_locator.by, element_locator.value)))
        return element

    def wait_for_presence_of_element(self, element_locator):
        element = WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((element_locator.by, element_locator.value)))
        return element
