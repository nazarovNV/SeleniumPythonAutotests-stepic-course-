from selenium import webdriver
import time
import os
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажимаю кнопку
    button = browser.find_element_by_css_selector(".trollface.btn.btn-primary")
    button.click()

    # Переключаемся на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # Получаем значение переменной х
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    # Подставляем в выражение значение х и получаем результат
    y = calc(x)

    # Вводим результат в поле под выражением
    input_result = browser.find_element_by_css_selector("#answer")
    input_result.send_keys(y)

    button = browser.find_element_by_css_selector("button.btn.btn-primary")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()