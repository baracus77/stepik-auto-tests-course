from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)


    x_element = browser.find_element_by_css_selector(".form-group > label > #input_value")
    x = x_element.text
    y = calc(x)
    field = browser.find_element_by_id('answer')
    field.send_keys(y)
    check = browser.find_element_by_css_selector('.form-check-custom > .form-check-label')
    check.click()
    radio = browser.find_element_by_css_selector('.form-radio-custom > .form-check-label').click()
    button = browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(20)
    browser.quit()
