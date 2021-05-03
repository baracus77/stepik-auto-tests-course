from selenium import  webdriver
import time

link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    fields = browser.find_elements_by_css_selector("input[type=text]")
    for field in fields:
        field.send_keys("Мой ответ")
    button = browser.find_element_by_css_selector('button')
    button.click()


finally:
    time.sleep(30)
    browser.quit()
