import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from faker import Faker
from locators import RegistrationLocators as Loc
from urls import BASE_URL

class TestRegistration:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get(BASE_URL)
        self.driver.quit()

def test_existed_person_registration(self):
        fake = Faker()
        email = fake.email()
        password = fake.password()

        self.driver.find_element(*Loc.LOGIN_BTN).click()
        self.driver.find_element(*Loc.NO_ACCOUNT_BTN).click()
        self.driver.find_element(*Loc.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*Loc.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*Loc.CONFIRM_PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*Loc.CREATE_ACCOUNT_BTN).click()

        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(Loc.USERNAME_TEXT))
        self.driver.quit()

        self.driver = webdriver.Chrome()
        self.driver.get(BASE_URL)

        self.driver.find_element(*Loc.LOGIN_BTN).click()
        self.driver.find_element(*Loc.NO_ACCOUNT_BTN).click()
        self.driver.find_element(*Loc.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*Loc.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*Loc.CONFIRM_PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*Loc.CREATE_ACCOUNT_BTN).click()

        error = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(Loc.ERROR_HINT))

        assert "Ошибка" in error.text
