import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from faker import Faker
from locators import RegistrationLocators as Loc
from urls import BASE_URL

class TestRegistration:
 def test_wrong_email_registration(self, driver):
        self.driver.find_element(*Loc.LOGIN_BTN).click()
        self.driver.find_element(*Loc.NO_ACCOUNT_BTN).click()
        self.driver.find_element(*Loc.EMAIL_INPUT).send_keys("***")
        self.driver.find_element(*Loc.CREATE_ACCOUNT_BTN).click()

        error = WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(Loc.ERROR_HINT))

        assert "Ошибка" in error.text
