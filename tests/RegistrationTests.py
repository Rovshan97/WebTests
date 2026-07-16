from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelperHelper
from pages.RecoveryPage import RecoveryPageHelperHelper
from pages.RegistrationPage import RegistrationPageHelperHelper

import allure


BASE_URL = "https://sn.rv-school.ru/"

@allure.suite("Проверка формы регистрации")
@allure.title("Проверка регистрации в рандомной стране")
def test_registration_random_country(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelperHelper(browser)
    LoginPage.click_registration()
    RegistrationPage = RegistrationPageHelperHelper(browser)
    RegistrationPage.select_registration_by_phone()
    RegistrationPage.select_random_country()
