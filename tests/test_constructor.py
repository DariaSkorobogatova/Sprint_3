from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from variables import *
from locators import *


class TestConstructor:

    def test_choose_sause_section(self, driver):
        driver.get(login_page)

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, enter_button)))

        driver.find_element(By.XPATH, input_email).send_keys(email_for_auth)
        driver.find_element(By.NAME, input_password).send_keys(passwd_for_auth)
        driver.find_element(By.XPATH, enter_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, main_page_make_order_button)))

        driver.find_element(By.XPATH, sause_section).click()

        assert 'current' in driver.find_element(By.XPATH, sause_section).get_attribute('class')

    def test_choose_filling_section(self, driver):
        driver.get(login_page)

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, enter_button)))

        driver.find_element(By.XPATH, input_email).send_keys(email_for_auth)
        driver.find_element(By.NAME, input_password).send_keys(passwd_for_auth)
        driver.find_element(By.XPATH, enter_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, main_page_make_order_button)))

        driver.find_element(By.XPATH, filling_section).click()

        assert 'current' in driver.find_element(By.XPATH, filling_section).get_attribute('class')

    def test_choose_bun_section(self, driver):
        driver.get(login_page)

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, enter_button)))

        driver.find_element(By.XPATH, input_email).send_keys(email_for_auth)
        driver.find_element(By.NAME, input_password).send_keys(passwd_for_auth)
        driver.find_element(By.XPATH, enter_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, main_page_make_order_button)))

        driver.find_element(By.XPATH, filling_section).click()

        driver.find_element(By.XPATH, bun_section).click()

        assert 'current' in driver.find_element(By.XPATH, bun_section).get_attribute('class')