from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure


class BasePageLocators:
    TOOLBAR_LOGO = (By.XPATH, '//*[@class="toolbar_custom-logo_img __light"]')
    VK_PROJECTS_BUTTON = (By.XPATH, '//*[@class="toolbar_nav_i_ic"]')
    VK_PROJECTS_MORE_BUTTON = (By.XPATH, '//*[@data-l="t,more"]')


class BasePageHelper:
    def __init__(self, driver):
        self.driver = driver


    def check_page(self):
        with allure.step("Проверяем корректность загрузки страницы"):
            self.attach_screenshot()
        self.find_element(BasePageLocators.TOOLBAR_LOGO)
        self.find_element(BasePageLocators.VK_PROJECTS_BUTTON)


    def find_element(self, locator, time=5):
         return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator), message = f"Не удалось найти элемент {locator}")


    def find_elements(self, locator, time=5):
         return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_all_elements_located(locator), message = f"Не удалось найти элементы {locator}")


    @allure.step('Открываем страницу')
    def get_url(self, url):
        return self.driver.get(url)

    @allure.step('Делаем скриншот')
    def attach_screenshot(self):
        allure.attach(self.driver.get_screenshot_as_png(),'скриншот',allure.attachment_type.PNG)

    @allure.step('Нажимаем кнопку экосистемы')
    def click_vk_projects_button(self):
        self.find_element(BasePageLocators.VK_PROJECTS_BUTTON).click()

    @allure.step('Нажимаем кнопку "Еще"')
    def click_vk_projects_more_button(self):
        self.find_element(BasePageLocators.VK_PROJECTS_MORE_BUTTON).click()

    @allure.step('Получаем айди вкладки')
    def get_windows_id(self, index):
        return self.driver.window_handles[index]

    @allure.step('Переключаем вкладку')
    def switch_window(self, window_id):
        self.driver.switch_to.window(window_id)