from base_app import BasePage
from selenium.webdriver.common.by import By


class FormSearchLocators:
    LOCATOR_FIRST_NAME_FIELD = (By.CSS_SELECTOR, "#firstName")
    LOCATOR_LAST_NAME_FIELD = (By.CSS_SELECTOR, "#lastName")
    LOCATOR_USER_EMAIL_FIELD = (By.CSS_SELECTOR, "#userEmail")
    LOCATOR_GENDER_RADIO = {
        'Male': (By.XPATH, "//*[@id='genterWrapper']/div[2]/div[1]/label"),
        'Female': (By.XPATH, "//*[@id='genterWrapper']/div[2]/div[2]/label"),
        'Other': (By.XPATH, "//*[@id='genterWrapper']/div[2]/div[3]/label")
    }
    LOCATOR_MOBILE_NUMBER_FIELD = (By.CSS_SELECTOR, "#userNumber")

    LOCATOR_BIRTHDAY_BUTTON = (By.CSS_SELECTOR, "#dateOfBirthInput")
    LOCATOR_MONTHS_BUTTON = (
        By.XPATH,
        '//*[@id="dateOfBirth"]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/select'
    )
    LOCATOR_YEAR_BUTTON = (By.XPATH, '//*[@id="dateOfBirth"]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/select')
    LOCATOR_SUBJECTS_FIELD = (By.ID, "subjectsInput")
    LOCATOR_HOBBIES_CHECKBOXES = {
        'Sports': (By.XPATH, "//*[@id='hobbiesWrapper']/div[2]/div[1]/label"),
        'Reading': (By.XPATH, "//*[@id='hobbiesWrapper']/div[2]/div[2]/label"),
        'Music': (By.XPATH, "//*[@id='hobbiesWrapper']/div[2]/div[3]/label")
    }
    LOCATOR_PICTURE_BUTTON = (By.ID, "uploadPicture")
    LOCATOR_ADDRESS_FIELD = (By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[9]/div[2]/textarea")
    LOCATOR_STATE_SELECT = (By.ID, "state")
    LOCATOR_CITY_SELECT = (By.ID, "city")
    LOCATOR_SUBMIT_BUTTON = (By.ID, "submit")


class SearchHelper(BasePage):

    def enter_word(self, locator, word):
        search_field = self.find_element(locator)
        search_field.click()
        search_field.send_keys(word)

    def enter_first_name(self, first_name):
        self.enter_word(FormSearchLocators.LOCATOR_FIRST_NAME_FIELD, first_name)

    def enter_last_name(self, last_name):
        self.enter_word(FormSearchLocators.LOCATOR_LAST_NAME_FIELD, last_name)

    def enter_email(self, email):
        self.enter_word(FormSearchLocators.LOCATOR_USER_EMAIL_FIELD, email)

    def choose_gender(self, gender):
        locator = FormSearchLocators.LOCATOR_GENDER_RADIO[gender]
        search_radio_button = self.find_element(locator)
        search_radio_button.click()

    def enter_mobile(self, mobile):
        self.enter_word(FormSearchLocators.LOCATOR_MOBILE_NUMBER_FIELD, mobile)

    def choose_component(self, locator):
        search_button = self.find_element(locator)
        search_button.click()

    def choose_birthdate(self, month, year, day):
        self.choose_component(FormSearchLocators.LOCATOR_BIRTHDAY_BUTTON)
        self.choose_component(FormSearchLocators.LOCATOR_MONTHS_BUTTON)
        self.choose_component((By.XPATH, f"//*[@id='dateOfBirth']//select/option[contains(text(), '{month}')]"))
        self.choose_component(FormSearchLocators.LOCATOR_YEAR_BUTTON)
        self.choose_component(
            (
                By.XPATH,
                f"//*[@id='dateOfBirth']//div[2]/select/option[contains(text(), '{year}')]"
            )
        )
        self.choose_component(
            (
                By.XPATH,
                (
                    f"//div[contains(@class, 'react-datepicker__day') and not(contains(@class, 'react-datepicker__day--outside-month'))"
                    f" and contains(@class, 'react-datepicker__day--0{day}')]"
                )
            )
        )

    def enter_subjects(self, subject):
        self.enter_word(FormSearchLocators.LOCATOR_SUBJECTS_FIELD, subject)
        self.choose_component((By.CLASS_NAME, "subjects-auto-complete__menu"))

    def choose_hobbies(self, hobby):
        locator = FormSearchLocators.LOCATOR_HOBBIES_CHECKBOXES[hobby]
        search_checkbox_button = self.find_element(locator)
        search_checkbox_button.click()

    def upload_file(self, locator, file_path):
        file_input = self.find_element(locator)
        file_input.send_keys(file_path)

    def add_image(self, path):
        self.upload_file(FormSearchLocators.LOCATOR_PICTURE_BUTTON, path)

    def enter_address(self, address):
        self.enter_word(FormSearchLocators.LOCATOR_ADDRESS_FIELD, address)

    def choose_state(self, state):
        self.choose_component(FormSearchLocators.LOCATOR_STATE_SELECT)
        self.choose_component((By.XPATH, f"//*[@id='state']/div[2]/div/div[contains(text(), '{state}')]"))

    def choose_city(self, city):
        self.choose_component(FormSearchLocators.LOCATOR_CITY_SELECT)
        self.choose_component((By.XPATH, f"//*[@id='city']/div[2]/div/div[contains(text(), '{city}')]"))

    def click_submit(self):
        self.choose_component(FormSearchLocators.LOCATOR_SUBMIT_BUTTON)