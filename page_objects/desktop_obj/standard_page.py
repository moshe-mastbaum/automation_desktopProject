from selenium.webdriver.common.by import By


zero = (By.NAME, "אפס")
one = (By.NAME, "אחת")
two = (By.NAME, "שתיים")
three = (By.NAME, "שלוש")
four = (By.NAME, "ארבע")
five = (By.NAME, "חמש")
six = (By.NAME, "שש")
seven = (By.NAME, "שבע")
eight = (By.NAME, "שמונה")
nine = (By.NAME, "תשע")
plus = (By.NAME, "ועוד")
minuse = (By.NAME, "פחות")
mult = (By.NAME, "הכפל ב")
divide = (By.NAME, "חלק ב")
equels = (By.NAME, "שווה")
result = (By.XPATH, "//*[@AutomationId='CalculatorResults']")
clear = (By.NAME, "נקה ערך")
clear1 = (By.NAME, "נקה")
backspace = (By.NAME, "Backspace")
trigo = (By.NAME, "טריגונומטריה")
cos = (By.NAME, "קוסינוס")

class StandardPage:
    def __init__(self, driver):
        self.driver=driver
    def get_digit(self, digit):
        return self.driver.find_element(By.NAME, digit)
    def zero(self):
        return self.driver.find_element(zero[0], zero[1])
    def one(self):
        return self.driver.find_element(one[0], one[1])
    def two(self):
        return self.driver.find_element(two[0], two[1])
    def three(self):
        return self.driver.find_element(three[0], three[1])
    def four(self):
        return self.driver.find_element(four[0], four[1])
    def five(self):
        return self.driver.find_element(five[0], five[1])
    def six(self):
        return self.driver.find_element(six[0], six[1])
    def seven(self):
        return self.driver.find_element(seven[0], seven[1])
    def eight(self):
        return self.driver.find_element(eight[0], eight[1])
    def nine(self):
        return self.driver.find_element(nine[0], nine[1])
    def plus(self):
        return self.driver.find_element(plus[0], plus[1])
    def minuse(self):
        return self.driver.find_element(minuse[0], minuse[1])
    def mult(self):
        return self.driver.find_element(mult[0], mult[1])
    def divide(self):
        return self.driver.find_element(divide[0], divide[1])
    def equels(self):
        return self.driver.find_element(equels[0], equels[1])
    def result(self):
        return self.driver.find_element(result[0], result[1])
    def clear(self):
        # print("pppppppp ",self.driver.find_element(clear[0], clear[1]))
        if len(self.driver.find_elements(clear[0], clear[1]))>0:
            return self.driver.find_element(clear[0], clear[1])
        else:
            return self.driver.find_element(clear1[0], clear1[1])

    def backspace(self):
        return self.driver.find_element(backspace[0], backspace[1])
    def trigo(self):
        return self.driver.find_element(trigo[0], trigo[1])
    def cos(self):
        return self.driver.find_element(cos[0], cos[1])
