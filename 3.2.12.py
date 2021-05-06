from selenium import webdriver
import unittest


class TestAbs(unittest.TestCase):
    def lName(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        name = browser.find_element_by_css_selector('div.first_block > .first_class > input.first')
        name.send_keys("Alex")
        lastName = browser.find_element_by_css_selector('div.first_block > .second_class > input.second')
        lastName.send_keys("Demidov")
        email = browser.find_element_by_css_selector('div.first_block > .third_class > input.third')
        email.send_keys("test@test.ru")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

if __name__ == "__main__":
    unittest.main()
