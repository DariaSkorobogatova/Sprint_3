from selenium.webdriver.common.by import By


class RegistrationLocators:
    input_name = [By.XPATH, './/label[text()="Имя"]/following-sibling::input']
    input_email = [By.XPATH, './/label[text()="Email"]/following-sibling::input']
    input_password = [By.NAME, 'Пароль']
    reg_button = [By.XPATH, './/button[text()="Зарегистрироваться"]']
    enter_button = [By.XPATH, './/button[text()="Войти"]']
    invalid_passwd_messg = [By.CSS_SELECTOR, '.input__error']
