from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.HelpPage import HelpPageHelperHelper, HelpPageLocators
from pages.AdvertisementCabinetHelp import AdvertisementCabinetHelpHelper

import allure

BASE_URL = 'https://ok.ru/help'

def test_help_test(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    HelpPage = HelpPageHelperHelper(browser)
    HelpPage.scrollToitem(HelpPageLocators.HELP_ADVERTISEMENT_CABINET)
    AdvertisementCabinetHelpHelper(browser)
