from data import *
from fixture.authorisation import Authorisation
from fixture.registration import Registration
from fixture.constructor import Constructor


class TestConstructor:

    def test_choose_sause_section(self, driver):
        auth = Authorisation(driver)
        cnstr = Constructor(driver)
        reg = Registration(driver)
        auth.go_to_login_page(login_page)
        reg.wait_for_enter_bt_is_clickable()
        auth.log_in(email_for_auth, passwd_for_auth)
        auth.wait_make_order_bt_is_clickable()
        cnstr.click_sause_section()
        assert 'current' in cnstr.get_attribute_sause_section()

    def test_choose_filling_section(self, driver):
        auth = Authorisation(driver)
        cnstr = Constructor(driver)
        reg = Registration(driver)
        auth.go_to_login_page(login_page)
        reg.wait_for_enter_bt_is_clickable()
        auth.log_in(email_for_auth, passwd_for_auth)
        auth.wait_make_order_bt_is_clickable()
        cnstr.click_filling_section()
        assert 'current' in cnstr.get_attribute_filling_section()

    def test_choose_bun_section(self, driver):
        auth = Authorisation(driver)
        cnstr = Constructor(driver)
        reg = Registration(driver)
        auth.go_to_login_page(login_page)
        reg.wait_for_enter_bt_is_clickable()
        auth.log_in(email_for_auth, passwd_for_auth)
        auth.wait_make_order_bt_is_clickable()
        cnstr.click_filling_section()
        cnstr.click_bun_section()
        assert 'current' in cnstr.get_attribute_bun_section()
