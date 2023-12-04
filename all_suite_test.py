import unittest
from unittest.loader import TestLoader


from test_cases.login_to_the_system_TC01 import TestLoginPage01
from test_cases.remind_password_TC02 import TestLoginPage02
from test_cases.change_language_TC03 import TestLoginPage03
from test_cases.dashboard_addplayer_TC04 import TestDashboard
from test_cases.fill_add_player_form_req_TC05 import TestAddPlayer01
from test_cases.fill_add_player_form_all_TC06 import TestAddPlayer02


def full_suite():
    test_suite = unittest.TestLoader()
    login_to_the_system_test = test_suite.loadTestsFromTestCase(TestLoginPage01)
    remind_password_test = test_suite.loadTestsFromTestCase(TestLoginPage02)
    change_language_test = test_suite.loadTestsFromTestCase(TestLoginPage03)
    dashboard_add_player_test = test_suite.loadTestsFromTestCase(TestDashboard)
    fill_add_player_req_test = test_suite.loadTestsFromTestCase(TestAddPlayer01)
    fill_add_player_all_test = test_suite.loadTestsFromTestCase(TestAddPlayer02)
    return unittest.TestSuite([login_to_the_system_test, remind_password_test, change_language_test, dashboard_add_player_test, fill_add_player_req_test, fill_add_player_all_test])


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())
