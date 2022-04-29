import time
from selenium.webdriver.common.keys import Keys
import allure
from extentions.ui_actions import UiAction

from utilities import manage_pages as page


class DesktopFlows:
    @staticmethod
    @allure.step('add new task')
    def add_task(self, task_name):
        UiAction.text_in(page.TaskPage.create(self), task_name)
        UiAction.text_in(page.TaskPage.create(self), Keys.RETURN)

    @staticmethod
    @allure.step('calculate expression')
    def calculate(self, expression):
        DesktopFlows.write(self, expression)
        UiAction.click(page.StandardPage.equels(self))

    def write(self, expression):
        for i in expression:
            DesktopFlows.calculator_click(self, i)

    @staticmethod
    def calculator_click(self, value):
        match value:
            case '0':
                return UiAction.click(page.StandardPage.zero(self)),
            case '1':
                return UiAction.click(page.StandardPage.one(self)),
            case '2':
                UiAction.click(page.StandardPage.two(self)),
            case '3':
                UiAction.click(page.StandardPage.three(self)),
            case '4':
                UiAction.click(page.StandardPage.four(self)),
            case '5':
                UiAction.click(page.StandardPage.five(self)),
            case '6':
                UiAction.click(page.StandardPage.six(self)),
            case '7':
                UiAction.click(page.StandardPage.seven(self)),
            case '8':
                UiAction.click(page.StandardPage.eight(self)),
            case '9':
                UiAction.click(page.StandardPage.nine(self)),
            case '+':
                UiAction.click(page.StandardPage.plus(self)),
            case '-':
                UiAction.click(page.StandardPage.minuse(self)),
            case '*':
                UiAction.click(page.StandardPage.mult(self)),
            case '/':
                UiAction.click(page.StandardPage.divide(self)),
            case '=':
                UiAction.click(page.StandardPage.equels(self))

    @staticmethod
    @allure.step('get result')
    def get_result(self):
        return page.StandardPage.result(self).text.replace("התצוגה היא", "").strip()

    @staticmethod
    @allure.step('trigo')
    def trigo(self, func, value):
        DesktopFlows.calculate(self, value)
        UiAction.click(page.StandardPage.trigo(self))
        UiAction.click(page.StandardPage.cos(self))
        UiAction.click(page.StandardPage.equels(self))

    @staticmethod
    @allure.step('backspace')
    def backspace(self):
        UiAction.click(page.StandardPage.backspace(self))

    def clear(self):
        UiAction.click(page.StandardPage.clear(self))