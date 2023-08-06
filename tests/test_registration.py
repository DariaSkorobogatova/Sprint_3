from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from variables import *
from locators import *
from helpers import generate_mail as mail


class TestRegistration:

    def test_registration_success(self, driver):
        driver.get(register_page)

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, input_name)))

        driver.find_element(By.XPATH, input_name).send_keys(name)
        driver.find_element(By.XPATH, input_email).send_keys(mail.generate())
        driver.find_element(By.NAME, input_password).send_keys(valid_password)

        driver.find_element(By.XPATH, reg_button).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, enter_button)))

        assert len(driver.find_elements(By.XPATH, enter_button)) == 1

    def test_short_invalid_passwd_message(self, driver):
        driver.get(register_page)

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, input_name)))

        driver.find_element(By.XPATH, input_name).send_keys(name)
        driver.find_element(By.XPATH, input_email).send_keys(mail.generate())
        driver.find_element(By.NAME, input_password).send_keys(invalid_password)

        driver.find_element(By.XPATH, reg_button).click()

        assert driver.find_element(By.CSS_SELECTOR, invalid_passwd_messg).text == 'Некорректный пароль'
