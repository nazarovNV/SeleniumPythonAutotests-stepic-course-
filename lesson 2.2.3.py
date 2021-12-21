from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    for element in browser.find_elements_by_css_selector("#num1"):
        x = element.text
    for element in browser.find_elements_by_css_selector("#num2"):
        y = element.text
    result = str(int(x)+int(y))
    print(result)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(result) # ищем элемент с текстом "Python"
    button = browser.find_element_by_css_selector("button.btn.btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()