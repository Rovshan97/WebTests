from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
from pages.RecoveryPage import RecoveryPageHelper
from pages.RegistrationPage import RegistrationPageHelper

import allure


BASE_URL = "https://sn.rv-school.ru/"

@allure.suite("Проверка формы регистрации")
@allure.title("Проверка регистрации в рандомной стране")
def test_registration_random_country(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.click_registration()
    RegistrationPage = RegistrationPageHelper(browser)
    RegistrationPage.select_registration_by_phone()
    RegistrationPage.select_random_country()