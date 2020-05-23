import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first = browser.find_element_by_xpath("//span[@id='num1']").text
    second = browser.find_element_by_xpath("//span[@id='num2']").text
    value = str(int(first) + int(second))
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(value)

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

