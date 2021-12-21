import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def test_input_text(expected_result, actual_result):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert expected_result==actual_result, f"expected {expected_result}, got {actual_result}"

expected_result2=input("Введите значение 1")
actual_result2=input("Введите значение 2")
test_input_text(expected_result2, actual_result2)
# Тест второго коммита