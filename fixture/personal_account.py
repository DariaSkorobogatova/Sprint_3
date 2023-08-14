from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.personal_account import PersonalAccountLocators as l


class PersonalAccount:
    def __init__(self, driver):
        self.driver = driver

    def wait_profile_loaded(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(tuple(l.profile)))

    def profile_bt_is_clickable(self):
        return self.driver.find_element(*l.profile).is_enabled()

    def click_constructor(self):
        self.driver.find_element(*l.constructor).click()

    def click_main_logo(self):
        self.driver.find_element(*l.main_logo).click()

    def click_logout_bt(self):
        self.driver.find_element(*l.logout_button).click()

