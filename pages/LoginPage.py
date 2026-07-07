from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

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
    ERROR_TEXT = (By.XPATH, '//*[@class="input-e login-error"]')