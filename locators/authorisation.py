from selenium.webdriver.common.by import By


class AuthorisationLocators:
    input_email = [By.XPATH, './/label[text()="Email"]/following-sibling::input']
    input_password = [By.NAME, 'Пароль']
    enter_button = [By.XPATH, './/button[text()="Войти"]']
    main_page_enter_acc_button = [By.XPATH, './/button[text()="Войти в аккаунт"]']
    main_page_make_order_button = [By.XPATH, './/button[text()="Оформить заказ"]']
    personal_acc = [By.XPATH, './/p[text()="Личный Кабинет"]']
    auth_link = [By.CSS_SELECTOR, '.Auth_link__1fOlj']