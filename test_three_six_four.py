import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://stepik.org/lesson/236895/step/1"

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

class AuthStepik():
    def test_auth_on_stepik(self, browser):
        browser.get(link)
        input1 = browser.find_element(By.CSS_SELECTOR, 'button[type = "submit"]')
        input1.click()
