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

    def test_create_post_authorized(self, driver):
        driver.find_element(*RLoc.LOGIN_BTN).click()
        driver.find_element(*RLoc.EMAIL_INPUT).send_keys(TEST_USER_EMAIL)
        driver.find_element(*RLoc.PASSWORD_INPUT).send_keys(TEST_USER_PASSWORD)
        driver.find_element(*RLoc.SUBMIT_BTN).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(RLoc.LOGOUT_BTN))

        driver.find_element(*CLoc.POST_BTN).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(CLoc.FORM_TITLE))

        driver.find_element(*CLoc.NAME_INPUT).send_keys("Новый товар")
        driver.find_element(*CLoc.DESCRIPTION_INPUT).send_keys("Новинка самого нового поколения")
        driver.find_element(*CLoc.PRICE_INPUT).send_keys("500")

        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(CLoc.OPEN_DROP_DOWN_CITY)).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(CLoc.CITY_OPTIONS))

        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(CLoc.CITY_OPTION_MSK)).click()

        driver.find_element(*CLoc.CONDITION_NEW_RADIO).click()

        publish_btn = WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(CLoc.PUBLISH_BTN))
        driver.execute_script("arguments[0].scrollIntoView(true);", publish_btn)
        driver.execute_script("arguments[0].click();", publish_btn)

        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(CLoc.MY_ADS_HEADER))

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(CLoc.AVATAR_BTN)).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(CLoc.PROFILE_HEADER))

        assert "Новый товар" in driver.page_source
