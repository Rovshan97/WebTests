from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import allure

class LoginPageLocators:
    LOGIN_TAB = (By.XPATH, '//*[@data-l="t,login_tab"]')
    QR_CODE = (By.XPATH, '//*[@data-l="t,qr_tab"]')
    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.ID, 'field_password')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-test-id="enter-action"]')
    LOGIN_BY_QR = (By.XPATH, '//*[@label="Войти по QR-коду"]')
    HIDE_PASSWORD = (By.XPATH, '//*[@aria-label="Не получается войти?"]')
    REGISTRATION = (By.XPATH, '//div[@class="LoginFormMain-module__bottom___YLtCo"]/button[@type="button"]')
    AUTHORIZATION_BY_VK = (By.XPATH, '//*[@data-l="t,vkc"]')
    AUTHORIZATION_BY_MAIL_RU = (By.XPATH, '//*[@data-l="t,mailru"]')
    AUTHORIZATION_BY_YANDEX = (By.XPATH, '//*[@data-l="t,yandex"]')
    OTHER_BUTTON = (By.XPATH, '//*[@data-l="t,other"]')
    ERROR_TEXT = (By.XPATH, '//*[@class="LoginForm-module__error___1xmAD vkuiCaption__sizeYNone vkuiCaption__level1 vkuiTypography__host vkuiTypography__normalize vkuiRootComponent__host"]')

class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        self.find_element(LoginPageLocators.LOGIN_TAB)
        self.find_element(LoginPageLocators.QR_CODE)
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.LOGIN_BY_QR)
        self.find_element(LoginPageLocators.HIDE_PASSWORD)
        self.find_element(LoginPageLocators.REGISTRATION)
        self.find_element(LoginPageLocators.AUTHORIZATION_BY_VK)
        self.find_element(LoginPageLocators.AUTHORIZATION_BY_MAIL_RU)
        self.find_element(LoginPageLocators.AUTHORIZATION_BY_YANDEX)

    @allure.step("Нажимаем на кнопку 'войти'")
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()


    @allure.step("Получаем текст ошибки")
    def get_text_error(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_TEXT).text

    @allure.step("Выбираем поле и вводим текст в это поле")
    def enter_login(self, text):
        login_field = self.find_element(LoginPageLocators.LOGIN_FIELD)
        login_field.send_keys(text)
        self.attach_screenshot()
