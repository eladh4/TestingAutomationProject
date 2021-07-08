from abc import ABC

from infra.pages.wrapper_driver import WrapperDriver


class AbstractPage(ABC):

    def __init__(self, driver):
        self.driver = driver
        self.wrapper_driver = WrapperDriver(driver)