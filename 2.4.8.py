from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.XPATH, "//h5[@id='price']"), '100'))
    button = browser.find_element(By.XPATH, "//button[@id='book']").click()


    x = browser.find_element(By.XPATH, "//span[@id='input_value']")
    answer = browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(calc(x.text))
    submit = browser.find_element(By.XPATH, "//button[@type='submit']").click()

    alert_text = browser.switch_to.alert.text.split(': ')[-1]
    alert = browser.switch_to.alert.accept()

    browser.get("https://stepik.org/catalog?auth=login")

    browser.implicitly_wait(4)

    email = browser.find_element(By.ID, 'id_login_email').send_keys('sparrowgtt@gmail.com')
    password = browser.find_element(By.id, 'id_login_password').send_keys('121065vvSS')
    login_ = browser.find_element(By.XPATH, '//button[text()="Войти"]').click()

    time.sleep(1.5)

    browser.get("https://stepik.org/lesson/181384/step/8?unit=156009")

    answer1 = browser.find_element(By.XPATH, '//textarea').send_keys(alert_text)

    browser.execute_script("window.scrollBy(0, 300);")

    time.sleep(1.5)

    submit3 = browser.find_element(By.XPATH, '//button[text()="Отправить"]').click()

finally:
    time.sleep(10)
    browser.quit()

