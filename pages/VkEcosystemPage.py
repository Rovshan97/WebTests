import allure
from selenium.webdriver.common.by import By
from pages.BasePage import BasePageHelper


class VkEcosystemPageLocators:
    VK_TITLE = (By.XPATH, '//*[@class="Header_logo__tL_od"]')



class VkProjectsPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step("Проверяем корректность загрузки страницы"):
            self.attach_screenshot()
        self.find_element(VkEcosystemPageLocators.VK_TITLE)