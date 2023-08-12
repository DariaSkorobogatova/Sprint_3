from variables import *
from helpers import generate_mail as mail
from fixture.registration import Registration


class TestRegistration:

    def test_registration_success(self, driver):
        reg = Registration(driver)
        reg.go_to_reg_page()
        reg.wait_for_page_to_load()
        reg.fill_reg_form(name, mail.generate(), valid_password)
        reg.click_reg_bt()
        reg.wait_for_enter_bt_is_clickable()
        assert reg.enter_bt_is_clickable()

    def test_short_invalid_passwd_message(self, driver):
        reg = Registration(driver)
        reg.go_to_reg_page()
        reg.wait_for_page_to_load()
        reg.fill_reg_form(name, mail.generate(), invalid_password)
        reg.click_reg_bt()
        assert reg.text_msg_if_passwd_invalid() == 'Некорректный пароль'