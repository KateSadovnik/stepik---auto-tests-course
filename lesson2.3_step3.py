import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector("button").click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_xpath("//span[@id='input_value']").text
    x = x_element
    y = calc(x)

    input1 = browser.find_element_by_css_selector("[id='answer']")
    input1.send_keys(y)

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

