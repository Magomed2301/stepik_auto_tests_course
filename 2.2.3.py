from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser.get(link)

    num1 = browser.find_element(By.CSS_SELECTOR, "#num1")
    number1 = num1.text
    num2 = browser.find_element(By.CSS_SELECTOR, "#num2")
    number2 = num2.text
    sum_num = int(number1) + int(number2)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum_num))

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
