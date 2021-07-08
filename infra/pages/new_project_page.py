import time

from selenium.webdriver.common.by import By

from infra.pages.abtract_page import AbstractPage
from infra.pages.project_overview_page import ProjectOverviewPage
from infra.web.element_locator import ElementLocator


def find_element_in_list_of_class_name_by_text(driver, required_text_in_element, class_name):
    elements_with_specific_class_name_list = driver.find_elements_by_class_name(class_name)

    for element in elements_with_specific_class_name_list:
        if required_text_in_element in element.text:
            return element


class NewProjectPage(AbstractPage):
    project_name_input = ElementLocator(By.ID, "formly_3_textInput_name_0")
    advanced_settings_button = ElementLocator(By.XPATH, '//*[@id="content"]/openproject-base/div/ui-view/op-new-project/op-dynamic-form/form/formly-form/formly-field[3]/op-dynamic-field-group-wrapper/fieldset/legend/button')
    project_description_text_box = ElementLocator(By.XPATH, '//*[@id="formly_9_formattableInput_description_1"]/div/op-ckeditor/div/div[2]/div/p')

    status_button = ElementLocator(By.XPATH, '//*[@id="formly_9_selectProjectStatusInput__links.status_4"]/div/div/div[3]/input')
    save_button = ElementLocator(By.XPATH, '//*[@id="content"]/openproject-base/div/ui-view/op-new-project/op-dynamic-form/form/div/button')

    def __init__(self, driver):
        super().__init__(driver)

    def write_project_name(self, project_name):
        self.wrapper_driver.send_keys(self.project_name_input, project_name)
        return self

    def click_on_advanced_settings(self):
        self.wrapper_driver.click(self.advanced_settings_button)
        return self

    def write_description(self, project_description):
        self.wrapper_driver.click(self.project_description_text_box)
        self.wrapper_driver.send_keys(self.project_description_text_box, project_description)
        return self

    def select_status(self, project_status):
        self.wrapper_driver.click(self.status_button)
        on_track_status = find_element_in_list_of_class_name_by_text(self.driver, project_status, "ng-option") #TODO: remain the function be generic
        on_track_status.click()
        return self

    def click_on_save_button(self) -> ProjectOverviewPage:
        self.wrapper_driver.click(self.save_button)
        time.sleep(3)
        return ProjectOverviewPage(self.driver)
