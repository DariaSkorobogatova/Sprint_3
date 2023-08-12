from variables import *
from fixture.authorisation import Authorisation
from fixture.registration import Registration
from fixture.personal_account import PersonalAccount


class TestPersonalAccount:

    def test_go_to_personal_account(self, driver):
        auth = Authorisation(driver)
        pc = PersonalAccount(driver)
        auth.go_to_main_page()
        auth.wait_for_page_to_load()
        auth.click_personal_acc_bt()
        auth.log_in(email_for_auth, passwd_for_auth)
        auth.wait_make_order_bt_is_clickable()
        auth.click_personal_acc_bt()
        pc.wait_profile_loaded()
        assert pc.profile_bt_is_clickable()

    def test_from_personal_acc_to_constructor(self, driver):
        auth = Authorisation(driver)
        pc = PersonalAccount(driver)
        reg = Registration(driver)
        auth.go_to_login_page()
        reg.wait_for_enter_bt_is_clickable()
        auth.log_in(email_for_auth, passwd_for_auth)
        auth.wait_make_order_bt_is_clickable()
        auth.click_personal_acc_bt()
        pc.wait_profile_loaded()
        pc.click_constructor()
        auth.wait_make_order_bt_is_clickable()
        assert auth.make_order_bt_is_clickable()

    def test_from_personal_acc_click_main_logo(self, driver):
        auth = Authorisation(driver)
        pc = PersonalAccount(driver)
        reg = Registration(driver)
        auth.go_to_login_page()
        reg.wait_for_enter_bt_is_clickable()
        auth.log_in(email_for_auth, passwd_for_auth)
        auth.wait_make_order_bt_is_clickable()
        auth.click_personal_acc_bt()
        pc.wait_profile_loaded()
        pc.click_main_logo()
        auth.wait_make_order_bt_is_clickable()
        assert auth.make_order_bt_is_clickable()

    def test_from_personal_acc_logout(self, driver):
        auth = Authorisation(driver)
        pc = PersonalAccount(driver)
        reg = Registration(driver)
        auth.go_to_login_page()
        reg.wait_for_enter_bt_is_clickable()
        auth.log_in(email_for_auth, passwd_for_auth)
        auth.wait_make_order_bt_is_clickable()
        auth.click_personal_acc_bt()
        pc.wait_profile_loaded()
        pc.click_logout_bt()
        reg.wait_for_enter_bt_is_clickable()
        assert reg.enter_bt_is_clickable()
