from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By
import allure

class LoginPageLocators:
    AUTHORIZATION = (By.XPATH, '//*[@name="hero-login-btn"]')
    REGISTRATION_BUTTON = (By.XPATH, '//*[@name="hero-register-btn"]')
    LOGIN_TAB = (By.XPATH, '//*[@name="tab-login"]')
    QR_TAB = (By.XPATH, '//*[@name="tab-qr"]')
    LOGIN_FIELD = (By.XPATH, '//*[@name="login-phone-email"]')
    PASSWORD_FIELD = (By.XPATH, '//*[@name="login-password"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@name="login-submit-btn"]')
    HIDE_PASSWORD = (By.XPATH, '//*[@name="forgot-password-link"]')
    ERROR_TEXT = (By.XPATH, '//*[@name="login-error"]')
    RECOVERY_BUTTON = (By.XPATH, '//*[@name="lockout-recover-btn"]')
    CANCEL_LINK = (By.XPATH, '//*[@name="lockout-cancel-btn"]')
    REGISTRATION_CANCEL = (By.XPATH, '//*[@name="lockout-register-btn"]')



class LoginPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step("Проверяем корректность загрузки страницы"):
            self.attach_screenshot()
        self.find_element(LoginPageLocators.AUTHORIZATION)
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_TAB)
        self.find_element(LoginPageLocators.QR_TAB)
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)

    @allure.step("Нажимаем на кнопку 'войти'")
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()


    @allure.step("Получаем текст ошибки")
    def get_text_error(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_TEXT).text

    @allure.step("Вводим логин в поле логин")
    def enter_login(self, login):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(login)
        self.attach_screenshot()

    @allure.step("Вводим пароль в поле пароль")
    def enter_password(self, password):
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.attach_screenshot()

    @allure.step("Переходим к восстановлению")
    def click_recovery(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.RECOVERY_BUTTON).click()


    @allure.step("Переходим к регистрации")
    def click_registration(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON).click()