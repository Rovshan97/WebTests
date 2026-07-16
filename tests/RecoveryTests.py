from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelperHelper
from pages.RecoveryPage import RecoveryPageHelperHelper
import allure

BASE_URL = "https://sn.rv-school.ru/"
LOGIN = "admin"
PASSWORD = "12"


@allure.suite("Проверка восстановления пользователя")
@allure.title("Проверка перехода к восстановлению после нескольких неудачных попыток входа")
def test_go_to_recovery_after_many_fails(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelperHelper(browser)
    LoginPage.enter_login(LOGIN)
    LoginPage.enter_password(PASSWORD)

    for i in range(3):
        LoginPage.click_login()

    LoginPage.click_recovery()
    RecoveryPageHelperHelper(browser)

