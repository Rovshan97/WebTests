from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By
import allure
import random

class RegistrationPageLocators:
    COUNTRY_LIST = (By.XPATH, '//*[@name="phone-country-select"]')
    COUNTRY_ITEM = (By.XPATH, '//*[starts-with(@data-test-id, "phone-country-option-")]')
    PHONE_FIELD = (By.XPATH, '//*[@name="phone-number-input"]')
    SEND_CODE_BUTTON = (By.XPATH, '//*[@name="phone-send-code-btn"]')
    BACK_TO_EMAIL_REGISTRATION = (By.XPATH, '//*[@name="phone-cancel-btn"]')
    LOGIN_LINK = (By.XPATH, '//*[@name="login-link-anchor"]')
    REGISTRATION_BY_PHONE = (By.XPATH, '//*[@name="register-phone-toggle"]')


class RegistrationPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver


    @allure.step("Выбираем рандомную страну")
    def select_random_country(self):
        self.find_element(RegistrationPageLocators.COUNTRY_LIST).click()
        country_items = self.find_elements(RegistrationPageLocators.COUNTRY_ITEM)
        random_number = random.randint(0, 39)
        country_items[random_number].click()
        selected_country = random.choice(country_items)
        selected_country.click()
        self.attach_screenshot()

    @allure.step("Нажимаем на кнопку 'Регистрация по телефону'")
    def select_registration_by_phone(self):
        self.find_element(RegistrationPageLocators.REGISTRATION_BY_PHONE).click()






