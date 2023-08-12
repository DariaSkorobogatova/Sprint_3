from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.registration import RegistrationLocators as l


class Registration:
    def __init__(self, driver):
        self.driver = driver

    def go_to_reg_page(self):
        self.driver.get('https://stellarburgers.nomoreparties.site/register')

    def fill_reg_form(self, name, email, passwd):
        self.driver.find_element(*l.input_name).send_keys(name)
        self.driver.find_element(*l.input_email).send_keys(email)
        self.driver.find_element(*l.input_password).send_keys(passwd)

    def click_reg_bt(self):
        self.driver.find_element(*l.reg_button).click()

    def wait_for_page_to_load(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(tuple(l.input_name)))

    def wait_for_enter_bt_is_clickable(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(tuple(l.enter_button)))

    def enter_bt_is_clickable(self):
        return self.driver.find_element(*l.enter_button).is_enabled()

    def text_msg_if_passwd_invalid(self):
        return self.driver.find_element(*l.invalid_passwd_messg).text
