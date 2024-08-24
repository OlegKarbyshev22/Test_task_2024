from selenium.webdriver.common.by import By
LOCATOR_GENDER_RADIO = {
        'Male': (By.ID, "gender-radio-1"),
        'Female': (By.ID, "gender-radio-2"),
        'Other': (By.ID, "gender-radio-3")
    }

print(LOCATOR_GENDER_RADIO['Male'])