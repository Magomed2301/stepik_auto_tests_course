import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")

    x = browser.find_element(By.ID, 'input_value')
    res = calc(x.text)
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(res)
    chck = browser.find_element(By.ID, 'robotCheckbox')
    chck.click()
    rdbttn = browser.find_element(By.ID, 'robotsRule')
    rdbttn.click()
    submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()
