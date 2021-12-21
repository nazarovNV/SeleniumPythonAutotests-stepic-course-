from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Получаем значение переменной х
    x_element = browser.find_element_by_css_selector ("#input_value")
    x = x_element.text
    #Подставляем в выражение значение х и получаем результат
    y = calc(x)
    #Скролим страницу до поля ввода
    inputPlace = browser.find_element_by_tag_name("input")
    browser.execute_script("return arguments[0].scrollIntoView(true);", inputPlace)
    inputPlace.click()
    #js script который нужно заэкзекьютить
    #button = document.getElementsByTagName("input")[0];
    #button.scrollIntoView(true);
    #Вводим результат в поле под выражением
    input_result = browser.find_element_by_css_selector("#answer")
    input_result.send_keys(y)

    input_checkbox = browser.find_element_by_css_selector("[for=\"robotCheckbox\"]")
    input_checkbox.click()

    # Нажимаем на радиобаттон
    input_radiobtn = browser.find_element_by_css_selector("[for = \"robotsRule\"]")
    input_radiobtn.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn.btn-primary")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()