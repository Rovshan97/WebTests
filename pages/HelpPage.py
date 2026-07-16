from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import allure

class HelpPageLocators:
    SEARCH_ANSWER = (By.XPATH, '//*[@data-tsid="help_search_input"]')
    QUICK_SEARCH_RESTORE_PROFILE = (By.XPATH, '//*[text()="восстановить профиль"]')
    QUICK_SEARCH_PASSWORD = (By.XPATH, '//*[text()="пароль"]')
    QUICK_SEARCH_UNBLOCK = (By.XPATH, '//*[text()="разблокировать"]')
    QUICK_SEARCH_PHOTO_WITH_THE_CODE = (By.XPATH, '//*[text()="фото с кодом"]')
    QUICK_SEARCH_REGISTRATION = (By.XPATH, '//*[text()="регистрация"]')
    HELP_ACTUAL_TODAY = (By.XPATH, '//*[text()="Сегодня актуально"]')
    HELP_REGISTRATION = (By.XPATH, '//*[text()="Регистрация"]')
    HELP_MY_PROFILE = (By.XPATH, '//*[text()="Мой профиль"]')
    HELP_COMMUNICATION = (By.XPATH, '//*[text()="Общение"]')
    HELP_ACCESS_TO_THE_PROFILE = (By.XPATH, '//*[text()="Доступ к профилю"]')
    HELP_SAFETY = (By.XPATH, '//*[text()="Безопасность"]')
    HELP_GROUPS = (By.XPATH, '//div[text()="Группы"]')
    HELP_PAID_FEATURES = (By.XPATH, '//*[text()="Платные функции"]')
    HELP_VIOLATIONS_AND_SPAM = (By.XPATH, '//*[text()="Нарушения и спам"]')
    HELP_GAMES_AND_APPS = (By.XPATH, '//*[text()="Игры и приложения"]')
    HELP_OTHER_SERVICES = (By.XPATH, '//*[text()="Другие сервисы"]')
    HELP_USEFUL_INFORMATION = (By.XPATH, '//*[text()="Полезная информация"]')
    HELP_ADVERTISEMENT_CABINET = (By.XPATH, '//*[text()="Рекламный кабинет"]')




class HelpPageHelperHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()


    def check_page(self):
        with allure.step("Проверяем корректность загрузки страницы"):
            self.attach_screenshot()
        self.find_element(HelpPageLocators.SEARCH_ANSWER)
        self.find_element(HelpPageLocators.QUICK_SEARCH_RESTORE_PROFILE)
        self.find_element(HelpPageLocators.QUICK_SEARCH_PASSWORD)
        self.find_element(HelpPageLocators.QUICK_SEARCH_UNBLOCK)
        self.find_element(HelpPageLocators.QUICK_SEARCH_PHOTO_WITH_THE_CODE)
        self.find_element(HelpPageLocators.QUICK_SEARCH_REGISTRATION)
        self.find_element(HelpPageLocators.HELP_ACTUAL_TODAY)
        self.find_element(HelpPageLocators.HELP_REGISTRATION)
        self.find_element(HelpPageLocators.HELP_MY_PROFILE)
        self.find_element(HelpPageLocators.HELP_COMMUNICATION)
        self.find_element(HelpPageLocators.HELP_ACCESS_TO_THE_PROFILE)
        self.find_element(HelpPageLocators.HELP_SAFETY)
        self.find_element(HelpPageLocators.HELP_GROUPS)
        self.find_element(HelpPageLocators.HELP_PAID_FEATURES)
        self.find_element(HelpPageLocators.HELP_VIOLATIONS_AND_SPAM)
        self.find_element(HelpPageLocators.HELP_GAMES_AND_APPS)
        self.find_element(HelpPageLocators.HELP_OTHER_SERVICES)
        self.find_element(HelpPageLocators.HELP_USEFUL_INFORMATION)
        self.find_element(HelpPageLocators.HELP_ADVERTISEMENT_CABINET)


    def scrollToitem(self, locator):
        scroll_item = self.find_element(locator)
        ActionChains(self.driver).scroll_to_element(scroll_item).click(scroll_item).perform()