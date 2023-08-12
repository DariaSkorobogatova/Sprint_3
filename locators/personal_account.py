from selenium.webdriver.common.by import By


class PersonalAccountLocators:
    profile = [By.XPATH, './/a[text()="Профиль"]']
    constructor = [By.XPATH, './/p[text()="Конструктор"]']
    main_logo = [By.CSS_SELECTOR, '.AppHeader_header__nav__g5hnF div']
    logout_button = [By.XPATH, './/button[text()="Выход"]']