import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestAbs(unittest.TestCase):

    def test_first_link_first(self):
        self.assertEqual("Congratulations! You have successfully registered!", "Congratulations! You have successfully registered!", "NoSuchElementException")
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input")
        input1.send_keys("qwerty")

        input2 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input")
        input2.send_keys("hello")

        input3 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input")
        input3.send_keys("test@mail.com")

        button = browser.find_element(By.CLASS_NAME, "btn-default")
        button.click()
        time.sleep(1)

    def test_first_link_two(self):
        self.assertEqual("Congratulations! You have successfully registered!", "Congratulations! You have successfully registered!", "NoSuchElementException")
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input")
        input1.send_keys("qwerty")

        input2 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input")
        input2.send_keys("hello")

        input3 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input")
        input3.send_keys("test@mail.com")

        button = browser.find_element(By.CLASS_NAME, "btn-default")
        button.click()
        time.sleep(1)


if __name__ == "__main__":
    unittest.main()
