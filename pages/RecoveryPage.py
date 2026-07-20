from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By
import allure

class RecoveryPageLocators:
    PHONE_BUTTON = (By.XPATH, '//*[@name="recovery-phone-btn"]')
    PHONE_LOST_BUTTON = (By.XPATH, '//*[@name="recovery-email-btn"]')
    QR_CODE = (By.XPATH, '//*[@name="qr-image"]')
    SUPPORT_BUTTON = (By.XPATH, '//*[@name="support-contact-btn"]')



class RecoveryPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        self.find_element(RecoveryPageLocators.PHONE_BUTTON).click()
        self.find_element(RecoveryPageLocators.PHONE_LOST_BUTTON).click()
        self.find_element(RecoveryPageLocators.SUPPORT_BUTTON).click()
        self.find_element(RecoveryPageLocators.QR_CODE).click()
