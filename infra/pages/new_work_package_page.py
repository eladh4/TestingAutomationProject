import time

from selenium.webdriver.common.by import By

from infra.pages.abtract_page import AbstractPage
from infra.web.element_locator import ElementLocator


class NewWorkPackagePage(AbstractPage):

    new_wp_part_type_button = ElementLocator(By.CSS_SELECTOR, "div.type [role='button']")
    new_wp_subject_text_box = ElementLocator(By.ID, "wp-new-inline-edit--field-subject")
    new_wp_description_text_box = ElementLocator(By.XPATH, "//div[@role='textbox']")
    new_wp_save_button = ElementLocator(By.ID, "work-packages--edit-actions-save")

    def __init__(self, driver):
        super().__init__(driver)

    def get_title(self):
        type_part = self.wrapper_driver.get_text(self.new_wp_part_type_button)
        return type_part

    def write_subject(self, subject):
        self.wrapper_driver.send_keys(self.new_wp_subject_text_box, subject)

    def write_description(self, description):
        self.wrapper_driver.send_keys(self.new_wp_description_text_box, description)

    def click_save_button(self):
        self.wrapper_driver.click(self.new_wp_save_button)
        from infra.pages.work_packages_page import WorkPackagesPage
        time.sleep(3)
        return WorkPackagesPage(self.driver)
