import time
import allure
import pytest
from extentions.verifications import Verifications
from workfows.desktop_flows import DesktopFlows


@pytest.mark.usefixtures('init_desktop_driver')
class Test_calculator:
    @allure.title('check calculate')
    @allure.description('check calculate')
    def test_check(self):
        DesktopFlows.calculate(self, '111+78*4')
        Verifications.verify_equals(DesktopFlows.get_result(self), '423')

    @allure.title('check backspace')
    @allure.description('check backspace')
    def test_backspace(self):
        DesktopFlows.write(self, '789')
        DesktopFlows.backspace(self)
        Verifications.verify_equals(DesktopFlows.get_result(self), '78')

    @allure.title('check backspace')
    @allure.description('check backspace')
    def test_clear(self):
        DesktopFlows.write(self, '789')
        DesktopFlows.clear(self)
        Verifications.verify_equals(DesktopFlows.get_result(self), '0')

    @allure.title('check division by zero')
    @allure.description('check division by zero')
    def test_division_by_zero(self):
        DesktopFlows.calculate(self, '111+78/0')
        Verifications.verify_equals(DesktopFlows.get_result(self), 'לא ניתן לחלק באפס')

    @allure.title('check trigonometry')
    @allure.description('check trigonometry')
    def test_trigonometry(self):
        DesktopFlows.trigo(self, 'cos', '60')
        Verifications.verify_equals(DesktopFlows.get_result(self), '0.5')

    def teardown_method(self):
        DesktopFlows.clear(self)
