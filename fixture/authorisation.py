from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.authorisation import AuthorisationLocators as l


class Authorisation:
    def __init__(self, driver):
        self.driver = driver

    def go_to_main_page(self):
        self.driver.get('https://stellarburgers.nomoreparties.site/')

    def wait_for_page_to_load(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(tuple(l.main_page_enter_acc_button)))

    def click_enter_acc_bt(self):
        self.driver.find_element(*l.main_page_enter_acc_button).click()

    def log_in(self, email_for_auth, passwd_for_auth):
        self.driver.find_element(*l.input_email).send_keys(email_for_auth)
        self.driver.find_element(*l.input_password).send_keys(passwd_for_auth)
        self.driver.find_element(*l.enter_button).click()

    def wait_make_order_bt_is_clickable(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(tuple(l.main_page_make_order_button)))

    def make_order_bt_is_clickable(self):
        return self.driver.find_element(*l.main_page_make_order_button).is_enabled()

    def click_personal_acc_bt(self):
        self.driver.find_element(*l.personal_acc).click()

    def wait_input_email_is_clickable(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(tuple(l.input_email)))

    def click_auth_link(self):
        self.driver.find_element(*l.auth_link).click()

    def go_to_forgot_passwd_page(self):
        self.driver.get('https://stellarburgers.nomoreparties.site/forgot-password')


