## 1_1
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#
#browser = webdriver.Chrome()
#browser.get("http://suninjuly.github.io/simple_form_find_task.html")
#button = browser.find_element(By.ID, "submit_button")

## 2_1
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#
#
#link = "http://suninjuly.github.io/simple_form_find_task.html"
#browser = webdriver.Chrome()
#browser.get(link)
#button = browser.find_element(By.ID, "submit_button")
#button.click()
#
## закрываем браузер после всех манипуляций
#browser.quit()

## 2_2
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#
#link = "http://suninjuly.github.io/simple_form_find_task.html"
#
#try:
#    browser = webdriver.Chrome()
#    browser.get(link)
#    button = browser.find_element(By.ID, "submit_button")
#    button.click()
#
#finally:
#    # закрываем браузер после всех манипуляций
#    browser.quit()

## 3_1
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#import time
#
#link = "http://suninjuly.github.io/simple_form_find_task.html"
#
#try:
#    browser = webdriver.Chrome()
#    browser.get(link)
#
#    input1 = browser.find_element(By.TAG_NAME, "input")
#    input1.send_keys("Ivan")
#    input2 = browser.find_element(By.NAME, "last_name")
#    input2.send_keys("Petrov")
#    input3 = browser.find_element(By.CLASS_NAME, "city")
#    input3.send_keys("Smolensk")
#    input4 = browser.find_element(By.ID, "country")
#    input4.send_keys("Russia")
#    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#    button.click()
#
#finally:
#    # успеваем скопировать код за 30 секунд
#    time.sleep(30)
#    # закрываем браузер после всех манипуляций
#    browser.quit()
#
## не забываем оставить пустую строку в конце файла


## 4_1
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#import math
#import time
#
#link1 = "http://suninjuly.github.io/find_link_text"
#site = str(math.ceil(math.pow(math.pi, math.e)*10000))
#
#
#try:
#    browser = webdriver.Chrome()
#    browser.get(link1)
#
#    link1 = browser.find_element(By.PARTIAL_LINK_TEXT, f"{site}")
#    link1.click()
#
#    input1 = browser.find_element(By.TAG_NAME, "input")
#    input1.send_keys("Ivan")
#    input2 = browser.find_element(By.NAME, "last_name")
#    input2.send_keys("Petrov")
#    input3 = browser.find_element(By.CLASS_NAME, "city")
#    input3.send_keys("Smolensk")
#    input4 = browser.find_element(By.ID, "country")
#    input4.send_keys("Russia")
#    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#    button.click()
#
#
#finally:
#    time.sleep(5)
#    browser.quit()


## 6_1
##
##from selenium import webdriver
##from selenium.webdriver.common.by import By
##import time
##
##try:
##    browser = webdriver.Chrome()
##    browser.get("http://suninjuly.github.io/huge_form.html")
##    elements = browser.find_elements(By.TAG_NAME, "input")
##    for element in elements:
##        element.send_keys("Мой ответ")
##
##    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
##    button.click()
##
##finally:
##    # успеваем скопировать код за 30 секунд
##    time.sleep(30)
##    # закрываем браузер после всех манипуляций
##    browser.quit()
##
## не забываем оставить пустую строку в конце файла


## 7_1
#
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#import time
#
#link = "http://suninjuly.github.io/find_xpath_form"
#
#try:
#    browser = webdriver.Chrome()
#    browser.get(link)
#
#    input1 = browser.find_element(By.TAG_NAME, "input")
#    input1.send_keys("Ivan")
#    input2 = browser.find_element(By.NAME, "last_name")
#    input2.send_keys("Petrov")
#    input3 = browser.find_element(By.CLASS_NAME, "city")
#    input3.send_keys("Smolensk")
#    input4 = browser.find_element(By.ID, "country")
#    input4.send_keys("Russia")
#    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
#    button.click()
#
#finally:
#    # успеваем скопировать код за 30 секунд
#    time.sleep(30)
#    # закрываем браузер после всех манипуляций
#    browser.quit()
#
## не забываем оставить пустую строку в конце файла

# 10_1
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, ".form-control.first:required")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, ".form-control.second:required")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, ".form-control.third:required")
    input3.send_keys("ivan@petrov.ru")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
