import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import RegistrationLocators as RLoc, CreatePostLocators as CLoc
from urls import BASE_URL
from tests.test_data import TEST_USER_EMAIL, TEST_USER_PASSWORD
