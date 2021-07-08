from selenium.webdriver.common.by import By

from infra.pages.abtract_page import AbstractPage
from infra.pages.new_work_package_page import NewWorkPackagePage
from infra.web.element_locator import ElementLocator


class WorkPackagesPage(AbstractPage):

    wp_title = ElementLocator(By.ID, "projects-menu")
    wp_rows_list = ElementLocator(By.XPATH, "//tbody//tr [@tabindex = '0']")
    wp_create_new_work_package_button = ElementLocator(By.CSS_SELECTOR, "button[aria-label='Create new work package']")
    wp_task_option = ElementLocator(By.CSS_SELECTOR, "a[aria-label='Task']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_project_title(self):
        return self.wrapper_driver.get_text(self.wp_title)

    def get_num_of_work_packages(self):
        work_packages_list = self.wrapper_driver.get_elements(self.wp_rows_list)
        return len(work_packages_list)

    def create_task_using_plus_create_button(self) -> NewWorkPackagePage:
        self.wrapper_driver.click(self.wp_create_new_work_package_button)
        self.wrapper_driver.click(self.wp_task_option)
        return NewWorkPackagePage(self.driver)

    def get_subject_of_work_package_in_row(self, number_of_work_package_row):
        if number_of_work_package_row >= 0:
            str_subject_xpath = f"//tbody//tr[{number_of_work_package_row}]//td[3]"
            wp_subject_of_work_package_in_row = ElementLocator(By.XPATH, str_subject_xpath)
            subject = self.wrapper_driver.get_text(wp_subject_of_work_package_in_row)
            return subject
        else:
            return None

    def get_type_of_work_package_in_row(self, number_of_work_package_row):
        if number_of_work_package_row >= 0:
            str_type_xpath = f"//tbody//tr[{number_of_work_package_row}]//td[4]"
            self.wp_type_of_work_package_in_row = ElementLocator(By.XPATH, str_type_xpath)
            type = self.wrapper_driver.get_text(self.wp_type_of_work_package_in_row)
            return type
        else:
            return None
