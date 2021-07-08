from selenium.webdriver.common.by import By

from infra.pages.abtract_page import AbstractPage
from infra.pages.work_packages_page import WorkPackagesPage
from infra.web.element_locator import ElementLocator


class ProjectOverviewPage(AbstractPage):

    work_packages_link_in_menu = ElementLocator(By.ID, "main-menu-work-packages")

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_work_packages_link_in_menu(self) -> WorkPackagesPage:
        self.wrapper_driver.click(self.work_packages_link_in_menu)
        return WorkPackagesPage(self.driver)
