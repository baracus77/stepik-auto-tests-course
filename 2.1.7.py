from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    picture = browser.find_element_by_tag_name("img")
    pictureAtribute = picture.get_attribute("valuex")
    x = pictureAtribute
    y = calc(x)
    field = browser.find_element_by_id('answer').send_keys(y)
    check = browser.find_element_by_id('robotCheckbox').click()
    radio = browser.find_element_by_id('robotsRule').click()
    button = browser.find_element_by_tag_name("button").click()

finally:
    time(5)
    browser.quit()
