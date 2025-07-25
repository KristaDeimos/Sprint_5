import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import RegistrationLocators as RLoc, CreatePostLocators as CLoc
from urls import BASE_URL
from tests.test_data import TEST_USER_EMAIL, TEST_USER_PASSWORD

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    yield driver
    driver.quit()
    
class TestCreatePost:
    def test_create_post_unauthorized(self, driver):
        driver.find_element(*CLoc.POST_BTN).click()

        modal_title = WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(CLoc.MODAL_AUTH_HEADER))

        assert "Чтобы разместить объявление, авторизуйтесь" in modal_title.text
