from selenium import webdriver
import time
import os


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Заполняем 3 поля
    input_Firstname = browser.find_element_by_css_selector("input[name='firstname']")
    input_Firstname.send_keys("Имя")

    input_Lastname = browser.find_element_by_css_selector("input[name='lastname']")
    input_Lastname.send_keys("Фамилия")

    input_Email = browser.find_element_by_css_selector("input[name='email']")
    input_Email.send_keys("эмейл")

    #Получаем путь к файлу который хотим прикрепить
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла

    addfile_button = browser.find_element_by_css_selector("input[type='file']")
    addfile_button.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn.btn-primary")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()