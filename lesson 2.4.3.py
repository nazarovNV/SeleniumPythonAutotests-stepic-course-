import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = browser.find_element_by_id("book")

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"100")
    )
    print("Цена норм")
    if price:
        button.click()
        print("Нажал")

        # Получаем значение переменной х
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    # Подставляем в выражение значение х и получаем результат
    y = calc(x)

    # Вводим результат в поле под выражением
    input_result = browser.find_element_by_css_selector("#answer")
    input_result.send_keys(y)

    button = browser.find_element_by_id("solve")
    button.click()
    # button.click()
    # message = browser.find_element_by_id("verify_message")

    # assert "successful" in message.text


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()