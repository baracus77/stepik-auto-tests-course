from selenium import webdriver
import time
import os


try:
    browser= webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    current_dir = os.path.abspath(os.path.dirname(__file__)) ####определяем директорию файла питона
    file_path = os.path.join(current_dir, 'file.txt')  ##присваиваем путь к файлу переменной

    firstName = browser.find_element_by_name('firstname').send_keys("Valera")
    lastName = browser.find_element_by_name("lastname").send_keys("Valera")
    email = browser.find_element_by_name("email").send_keys("Valera@ggg.com")
    addFile = browser.find_element_by_id("file").send_keys(file_path) #####загружаем файл
    btn = browser.find_element_by_tag_name("button").click()




finally:
    time(5)
    browser.quit()