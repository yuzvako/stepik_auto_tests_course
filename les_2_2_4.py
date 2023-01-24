#rom selenium import webdriver

#rowser = webdriver.Chrome()
#browser.execute_script("alert('Robots at work');")
#browser.execute_script("document.title='Script executing';")
#rowser.execute_script("document.title='Script executing';alert('Robots at work');")

#import math
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#import time
#
#def calc(x):
#  return str(math.log(abs(12*math.sin(int(x)))))
#
#try:
#    link = "http://suninjuly.github.io/execute_script.html"
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
#    browser.execute_script("window.scrollBy(0, 100);")
#
#    check = browser.find_element(By.ID, 'robotCheckbox')
#    check.click()
#
#    radio = browser.find_element(By.ID, 'robotsRule')
#    radio.click()
#
#    button = browser.find_element(By.TAG_NAME, "button")
#    button.click()
#
#finally:
#    time.sleep(5)
#    browser.quit()

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:

    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input_first_name = browser.find_element(By.NAME, 'firstname')
    input_first_name.send_keys('Иван')

    input_last_name = browser.find_element(By.NAME, 'lastname')
    input_last_name.send_keys('Петров')

    input_email = browser.find_element(By.NAME, 'email')
    input_email.send_keys('ivan@petrov.ru')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

finally:
    time.sleep(10)
    browser.quit()