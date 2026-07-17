from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.VkEcosystemPage import VkProjectsPageHelper
import allure

BASE_URL = 'https://ok.ru/'

@allure.suite("Проверка тулбара")
@allure.title("Переход к проектам экосистемы VK ")
def test_open_vk_ecosystem(browser):
    BasePage = BasePageHelper(browser)
    BasePage.get_url(BASE_URL)
    BasePage.check_page()

    current_window_id = BasePage.get_windows_id(0)
    BasePage.click_vk_projects_button()
    BasePage.click_vk_projects_more_button()

    new_window_id = BasePage.get_windows_id(1)
    BasePage.switch_window(new_window_id)

    VkEcosystemPage = VkProjectsPageHelper(browser)
    BasePage.switch_window(current_window_id)

    BasePageHelper(browser)
