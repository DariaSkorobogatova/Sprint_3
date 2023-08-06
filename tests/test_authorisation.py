from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from variables import *
from locators import *
from helpers import generate_mail as mail

email = mail.generate()


class TestAuth:

    def test_auth_from_main_page(self, driver):
        driver.get(main_page)

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, main_page_enter_acc_button)))

        driver.find_element(By.XPATH, main_page_enter_acc_button).click()

        driver.find_element(By.XPATH, input_email).send_keys(email_for_auth)
        driver.find_element(By.NAME, input_password).send_keys(passwd_for_auth)
        driver.find_element(By.XPATH, enter_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, main_page_make_order_button)))

        assert len(driver.find_elements(By.XPATH, main_page_make_order_button)) == 1

    def test_auth_via_personal_acc(self, driver):
        driver.get(main_page)

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, main_page_enter_acc_button)))

        driver.find_element(By.XPATH, personal_acc).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, input_email)))

        driver.find_element(By.XPATH, input_email).send_keys(email_for_auth)
        driver.find_element(By.NAME, input_password).send_keys(passwd_for_auth)
        driver.find_element(By.XPATH, enter_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, main_page_make_order_button)))

        assert len(driver.find_elements(By.XPATH, main_page_make_order_button)) == 1

    def test_auth_via_enter_link_on_registration_page(self, driver):
        driver.get(register_page)

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, input_name)))

        driver.find_element(By.CSS_SELECTOR, auth_link).click()

        driver.find_element(By.XPATH, input_email).send_keys(email_for_auth)
        driver.find_element(By.NAME, input_password).send_keys(passwd_for_auth)
        driver.find_element(By.XPATH, enter_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, main_page_make_order_button)))

        assert len(driver.find_elements(By.XPATH, main_page_make_order_button)) == 1

    def test_auth_via_forgot_passwd_link_on_login_page(self, driver):
        driver.get(forgot_passwd_page)

        driver.find_element(By.CSS_SELECTOR, auth_link).click()

        driver.find_element(By.XPATH, input_email).send_keys(email_for_auth)
        driver.find_element(By.NAME, input_password).send_keys(passwd_for_auth)
        driver.find_element(By.XPATH, enter_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, main_page_make_order_button)))

        assert len(driver.find_elements(By.XPATH, main_page_make_order_button)) == 1

