from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from variables import *
from locators import *


class TestPersonalAccount:

    def test_go_to_personal_account(self, driver):
        driver.get(main_page)

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, main_page_enter_acc_button)))

        driver.find_element(By.XPATH, personal_acc).click()

        driver.find_element(By.XPATH, input_email).send_keys(email_for_auth)
        driver.find_element(By.NAME, input_password).send_keys(passwd_for_auth)
        driver.find_element(By.XPATH, enter_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, main_page_make_order_button)))

        driver.find_element(By.XPATH, personal_acc).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, profile)))

        assert len(driver.find_elements(By.XPATH, profile)) == 1

    def test_from_personal_acc_to_constructor(self, driver):
        driver.get(login_page)

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, enter_button)))

        driver.find_element(By.XPATH, input_email).send_keys(email_for_auth)
        driver.find_element(By.NAME, input_password).send_keys(passwd_for_auth)
        driver.find_element(By.XPATH, enter_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, main_page_make_order_button)))

        driver.find_element(By.XPATH, personal_acc).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, profile)))

        driver.find_element(By.XPATH, constructor).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, main_page_make_order_button)))

        assert len(driver.find_elements(By.XPATH, main_page_make_order_button)) == 1

    def test_from_personal_acc_click_main_logo(self, driver):
        driver.get(login_page)

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, enter_button)))

        driver.find_element(By.XPATH, input_email).send_keys(email_for_auth)
        driver.find_element(By.NAME, input_password).send_keys(passwd_for_auth)
        driver.find_element(By.XPATH, enter_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, main_page_make_order_button)))

        driver.find_element(By.XPATH, personal_acc).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, profile)))

        driver.find_element(By.CSS_SELECTOR, main_logo).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, main_page_make_order_button)))

        assert len(driver.find_elements(By.XPATH, main_page_make_order_button)) == 1

    def test_from_personal_acc_logout(self, driver):
        driver.get(login_page)

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, enter_button)))

        driver.find_element(By.XPATH, input_email).send_keys(email_for_auth)
        driver.find_element(By.NAME, input_password).send_keys(passwd_for_auth)
        driver.find_element(By.XPATH, enter_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, main_page_make_order_button)))

        driver.find_element(By.XPATH, personal_acc).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, profile)))

        driver.find_element(By.XPATH, logout_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, enter_button)))

        assert len(driver.find_elements(By.XPATH, enter_button)) == 1

