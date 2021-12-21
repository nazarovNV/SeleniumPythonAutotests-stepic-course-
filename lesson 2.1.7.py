from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_number = browser.find_element_by_css_selector ("#num1")
    x_value=x_number.text
    print(x_value)
    input_element=browser.find_element_by_css_selector("input#answer")
    input_element.send_keys(calc(x_value))
    input_checkbox = browser.find_element_by_css_selector("input.check-input")
    input_checkbox.click()
    input_radiobtn = browser.find_element_by_css_selector("input#robotsRule.check-input")
    input_radiobtn.click()
    button = browser.find_element_by_css_selector("button.btn.btn-default")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()