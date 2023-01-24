from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.ID, 'answer')
    input.send_keys(f'{y}')

    button_submit = browser.find_element(By.TAG_NAME, 'button')
    button_submit.click()

finally:
    time.sleep(10)
    browser.quit()