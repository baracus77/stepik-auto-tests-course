from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100")) #поиск элементы со значением 100
    buy = browser.find_element_by_id("book").click()
    x = browser.find_element_by_id('input_value').text
    y = calc(x)
    field = browser.find_element_by_id("answer").send_keys(y)
    btn = browser.find_element_by_id("solve").click()



finally:
    time(10)
    browser.quit()
