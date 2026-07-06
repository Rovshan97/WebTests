from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_FIELD = (By.ID, 'field_email')
    LOGIN_BUTTON = (By.DATA-TEST-ID, 'enter-action')
    PASSWORD_FIELD = (By.ID, 'field_password')
    HIDE_PASSWORD = (By.XPATH, //*[@id="tabpanel-login-647130740"]/vkid-form-adapter/div/div/div/div/div[1]/form/div[2]/span/div/div[2]/span/button)
    QR_CODE = (By.DATA-L, 't,qr_tab')
    LOGIN_BY_QR = (By.LABEL, 'Войти по QR-коду')
    FORGOT_YOUR_PASSWORD = (By.ARIA-LABEL, 'Не получается войти?')
    REGISTRATION = (By.XPATH, '//*[@id="tabpanel-login-647130740"]/vkid-form-adapter/div/div/div/div/div[3]/button')
    AUTHORIZATION_BY_VK = (By.DATA-L, 't,vkc')
    AUTHORIZATION_BY_MAIL_RU = (By.DATA-L, 't,mailru')
    AUTHORIZATION_BY_YANDEX = (By.DATA-L, 't,yandex')

class LoginPageHelper(BasePage):
    pass

