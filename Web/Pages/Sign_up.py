from Web.Locators.Sign_up import SignUpLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver



class SignUp_function:
    def __init__(self, driver):
        self.driver = driver
        self.first_nameField = SignUpLocators.first_nameField
        self.last_nameField = SignUpLocators.last_nameField
        self.phoneOrEmailField = SignUpLocators.phoneOrEmailField
        self.email_confirmation = SignUpLocators.email_confirmation
        self.passwordNewField = SignUpLocators.passwordNewField
        self.birthdayField_day = SignUpLocators.birthdayField_day
        self.birthdayField_month = SignUpLocators.birthdayField_month
        self.birthdayField_years = SignUpLocators.birthdayField_year
        self.genderField_female = SignUpLocators.genderField_female
        self.genderField_male = SignUpLocators.genderField_male
        self.genderField_custom = SignUpLocators.genderField_custom
        self.signUpButton = SignUpLocators.signUpButton
        self.resultMessage = SignUpLocators.resultMessage
        self.BodyPronounField = SignUpLocators.BodyPronounField

    def creating_a_new_account(self):
        self.driver.find_element(By.XPATH,"//a[contains(text(),'יצירת חשבון חדש')]").click()


    def enter_name(self ):
        self.driver.find_element(By.NAME, self.first_nameField).send_keys()

    def enter_lastName(self, lastname):
        self.driver.find_element(By.NAME, self.last_nameField).send_keys(lastname)

    def enter_phoneOrEmail(self, phoneOrEmail):
        self.driver.find_element(By.NAME, self.phoneOrEmailField).send_keys(phoneOrEmail)

    def enter_emailConfirmation(self, email):
        self.driver.find_element(By.NAME, self.email_confirmation).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.passwordNewField).send_keys(password)

    def selectBirthday(self, field):
        if field == "day":
            return self.driver.find_element(By.ID, self.birthdayField_day)
        if field == 'month':
            return self.driver.find_element(By.ID, self.birthdayField_month)
        if field == 'year':
            return self.driver.find_element(By.ID, self.birthdayField_years)

    def selectGender(self, gender):
        if gender == "female":
            self.driver.find_element(By.CLASS_NAME, self.genderField_female).click()
        if gender == "male":
            self.driver.find_element(By.CSS_SELECTOR, self.genderField_male).click()
        if gender == "custom":
            self.driver.find_element(By.CSS_SELECTOR, self.genderField_custom).click()

    def selectBodyPronounField(self,x):
        if x == "y":
            return self.driver.find_element(By.XPATH, self.BodyPronounField)

    def clickOnSignUpButton(self):
        self.driver.find_element(By.NAME, self.signUpButton).click()

    def resultMessageSuccess(self):
        return self.driver.find_element(By.NAME, self.resultMessage).get_attribute("innerText")

    def resultMessageUnsuccess_firstName(self):
        return self.driver.find_element(By.XPATH, "//body[1]/div[6]/div[1]/div[1]/div[1]").get_attribute("innerText")

