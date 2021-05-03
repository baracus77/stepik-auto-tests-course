from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    link1= browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link1.click()
    input1 = browser.find_element_by_name('first_name')  # поиск по тегу
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")  # поиск по имени
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name('city')  # поиск по классу
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id('country')  # поиск по id
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")  # поиск по css классу
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()