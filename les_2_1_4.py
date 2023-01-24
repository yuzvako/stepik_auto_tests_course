#import math
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#import time
#
#def calc(x):
#  return str(math.log(abs(12*math.sin(int(x)))))
#
#try:
#    link = 'https://suninjuly.github.io/math.html'
#    browser = webdriver.Chrome()
#    browser.get(link)
#
#    x_element = browser.find_element(By.ID, 'input_value')
#    x = x_element.text
#    y = calc(x)
#
#    input1 = browser.find_element(By.ID, 'answer')
#    input1.send_keys(f'{y}')
#
#    check = browser.find_element(By.ID, 'robotCheckbox')
#    check.click()
#
#    radio = browser.find_element(By.ID, 'robotsRule')
#    radio.click()
#
#    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
#    button.click()
#
#finally:
#    time.sleep(10)
#    browser.quit()


#from selenium import webdriver
#from selenium.webdriver.common.by import By
#import time
#
#try:
#    link = 'https://suninjuly.github.io/math.html'
#    browser = webdriver.Chrome()
#    browser.get(link)
#
#    people_radio = browser.find_element(By.ID, "peopleRule")
#
#    people_checked = people_radio.get_attribute("checked")
#    print("value of people radio: ", people_checked)
#
#    robots_radio = browser.find_element(By.ID, "robotsRule")
#    robots_checked = robots_radio.get_attribute("checked")
#    print("value of people radio: ", robots_checked)
#    #assert people_checked is not None, "People radio is not selected by default"
#    assert people_checked == "true", "People radio is not selected by default"
#    assert robots_checked is None
#
#
#finally:
#    time.sleep(10)
#    browser.quit()

import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(f'{y}')

    check = browser.find_element(By.ID, 'robotCheckbox')
    check.click()

    radio = browser.find_element(By.ID, 'robotsRule')
    radio.click()

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

finally:
    time.sleep(5)
    browser.quit()