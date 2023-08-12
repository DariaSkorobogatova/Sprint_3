from variables import *
from fixture.authorisation import Authorisation
from fixture.registration import Registration


class TestAuth:

    def test_auth_from_main_page(self, driver):
        auth = Authorisation(driver)
        auth.go_to_main_page()
        auth.wait_for_page_to_load()
        auth.click_enter_acc_bt()
        auth.log_in(email_for_auth, passwd_for_auth)
        auth.wait_make_order_bt_is_clickable()
        assert auth.make_order_bt_is_clickable()

    def test_auth_via_personal_acc(self, driver):
        auth = Authorisation(driver)
        auth.go_to_main_page()
        auth.wait_for_page_to_load()
        auth.click_personal_acc_bt()
        auth.log_in(email_for_auth, passwd_for_auth)
        auth.wait_make_order_bt_is_clickable()
        assert auth.make_order_bt_is_clickable()

    def test_auth_via_enter_link_on_registration_page(self, driver):
        auth = Authorisation(driver)
        reg = Registration(driver)
        reg.go_to_reg_page()
        reg.wait_for_page_to_load()
        auth.click_auth_link()
        auth.log_in(email_for_auth, passwd_for_auth)
        auth.wait_make_order_bt_is_clickable()
        assert auth.make_order_bt_is_clickable()

    def test_auth_via_enter_link_on_forgot_passwd_page(self, driver):
        auth = Authorisation(driver)
        auth.go_to_forgot_passwd_page()
        auth.wait_input_email_is_clickable()
        auth.click_auth_link()
        auth.log_in(email_for_auth, passwd_for_auth)
        auth.wait_make_order_bt_is_clickable()
        assert auth.make_order_bt_is_clickable()


