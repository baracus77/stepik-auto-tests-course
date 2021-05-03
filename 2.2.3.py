from selenium import webdriver
import time


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_id("num1").text
    y = browser.find_element_by_id("num2").text
    z = str(int(x) + int(y))
    print(z)
    select = browser.find_element_by_tag_name("select").click()
    value = browser.find_element_by_css_selector(f"[value = '{z}']").click()
    button = browser.find_element_by_tag_name("button").click()


finally:
    time(5)
    browser.quit()
