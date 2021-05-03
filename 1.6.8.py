from selenium import  webdriver
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name('first_name')  # поиск по тегу
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")  # поиск по имени
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name('city')  # поиск по классу
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id('country')  # поиск по id
    input4.send_keys("Russia")
    button = browser.find_element_by_xpath("/html/body/div/form/div[6]/button[3]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

