import time
from selenium import webdriver
import unittest


class TestAbs(unittest.TestCase):
    def test_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector("div.first_block>div.first_class>input.first")
        input1.send_keys("Николай")
        input2 = browser.find_element_by_css_selector("div.first_block>div.second_class>input.second")
        input2.send_keys("Назаров")
        input3 = browser.find_element_by_css_selector("div.first_block>div.third_class>input.third")
        input3.send_keys("nikolaynazarovvv216@gmail.com")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",
                         "Should be 'Congratulations! You have successfully registered!'")

    def test_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector("div.first_block>div.first_class>input.first")
        input1.send_keys("Николай")
        input2 = browser.find_element_by_css_selector("div.first_block>div.second_class>input.second")
        input2.send_keys("Назаров")
        input3 = browser.find_element_by_css_selector("div.first_block>div.third_class>input.third")
        input3.send_keys("nikolaynazarovvv216@gmail.com")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",
                         "Should be 'Congratulations! You have successfully registered!'")


if __name__ == "__main__":
    unittest.main()

