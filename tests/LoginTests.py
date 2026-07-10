from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
import allure

BASE_URL = "https://sn.rv-school.ru/"
EMPTY_LOGIN_ERROR = "Введите телефон, email или логин и пароль."
EMPTY_PASSWORD_ERROR = "Введите телефон, email или логин и пароль."
LOGIN = "admin"
PASSWORD = "12"


@allure.suite("Проверка формы авторизации")
@allure.title("Проверка ошибки при пустой форме авторизации")
def test_empty_login_and_password(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.click_login()
    assert LoginPage.get_text_error() == EMPTY_LOGIN_ERROR


@allure.suite("Проверка формы авторизации")
@allure.title("Проверка ошибки при пустом поле пароль")
def test_empty_password_error(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.enter_login(LOGIN)
    LoginPage.click_login()
    assert LoginPage.get_text_error() == EMPTY_PASSWORD_ERROR