from selenium.webdriver.common.by import By

from infra.pages.abtract_page import AbstractPage
from infra.pages.new_project_page import NewProjectPage
from infra.pages.project_overview_page import ProjectOverviewPage
from infra.pages.work_packages_page import WorkPackagesPage
from infra.web.element_locator import ElementLocator


def find_element_in_list_of_class_name_by_text(driver, class_name, project_name_should_be_chosen):
    elements_with_specific_class_name_list = driver.find_elements_by_class_name(class_name)

    for element in elements_with_specific_class_name_list:
        if project_name_should_be_chosen in element.text:
            return element


class HomePage(AbstractPage):

    plus_project_button = ElementLocator(By.XPATH, '//*[@id="content"]/section[1]/div[2]/div[2]/a[1]/span')
    select_project_button = ElementLocator(By.ID, "projects-menu")
    work_packages_button = ElementLocator(By.ID, "main-menu-work-packages")

    def __init__(self, driver):
        super().__init__(driver)

    def click_new_project_using_plus_project_button(self) -> NewProjectPage:
        self.wrapper_driver.click(self.plus_project_button)
        return NewProjectPage(self.driver)

    def click_select_a_project_button(self, project_name_should_be_chosen) -> ProjectOverviewPage:
        self.wrapper_driver.click(self.select_project_button)
        selected_project = find_element_in_list_of_class_name_by_text(self.driver,
                                                                      "ui-matched-item",
                                                                      project_name_should_be_chosen)#TODO: remain the function be generic
        selected_project.click()
        return ProjectOverviewPage(self.driver)

    def click_work_packages_button(self) -> WorkPackagesPage:
        self.wrapper_driver.click(self.work_packages_button)
        return WorkPackagesPage(self.driver)
