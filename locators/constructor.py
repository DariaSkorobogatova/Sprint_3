from selenium.webdriver.common.by import By


class ConstructorLocators:
    sause_section = [By.XPATH, './/span[text()="Соусы"]/parent::div']
    filling_section =[By.XPATH, './/span[text()="Начинки"]/parent::div']
    bun_section = [By.XPATH, './/span[text()="Булки"]/parent::div']
