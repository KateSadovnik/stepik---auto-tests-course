import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_xpath("//img[@id='treasure']")
    value_treasure = x_element.get_attribute("valuex")
    x = value_treasure
    y = calc(x)

    input1 = browser.find_element_by_css_selector("[id='answer']")
    input1.send_keys(y)
    checkbox = browser.find_element_by_css_selector("[id='robotCheckbox']")
    checkbox.click()
    radiobutton = browser.find_element_by_css_selector("[id='robotsRule']")
    radiobutton.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

