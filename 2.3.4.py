from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser= webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    step1= browser.find_element_by_tag_name("button").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = browser.find_element_by_id('input_value').text
    y = calc(x)
    field = browser.find_element_by_id("answer").send_keys(y)
    btn = browser.find_element_by_tag_name("button").click()



finally:
    time(5)
    browser.quit()