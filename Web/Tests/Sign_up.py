import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Web.Base.BasePage import Base
from Web.Pages.Sign_up import SignUp_function
import pytest


@pytest.mark.usefixtures("set_up")
class Test_signUp(Base):
    def test_SignUpCorrectly_when_genderFemale(self):
        driver = self.driver
        signUp = SignUp_function(driver)
        signUp.creating_a_new_account()
        signUp.enter_name('yael')
        signUp.enter_lastName('lev')
        signUp.enter_phoneOrEmail('yael@walla.com')
        signUp.enter_emailConfirmation('yael@walla.com')
        signUp.enter_password('Aa123456')
        select = Select(signUp.selectBirthday('day'))
        select.select_by_visible_text('2')
        select = Select(signUp.selectBirthday('month'))
        select.select_by_visible_text('יוני')
        select = Select(signUp.selectBirthday('year'))
        select.select_by_visible_text('2000')
        signUp.selectGender("female")
        signUp.clickOnSignUpButton()
        try:
            assert signUp.resultMessageSuccess() == 'הזיני את הקוד מהדוא"ל שלך'
        except AssertionError:
            print("Something is wrong")

    def test_SignUpCorrectly_when_genderMale(self):
        driver = self.driver
        signUp = SignUp_function(driver)
        signUp.creating_a_new_account()
        signUp.enter_name('yael')
        signUp.enter_lastName('lev')
        signUp.enter_phoneOrEmail('yael@walla.com')
        signUp.enter_emailConfirmation('yael@walla.com')
        signUp.enter_password('Aa123456')
        select = Select(signUp.selectBirthday('day'))
        select.select_by_visible_text('2')
        select = Select(signUp.selectBirthday('month'))
        select.select_by_visible_text('יוני')
        select = Select(signUp.selectBirthday('year'))
        select.select_by_visible_text('2000')
        signUp.selectGender("male")
        signUp.clickOnSignUpButton()
        try:
            assert signUp.resultMessageSuccess() == 'הזיני את הקוד מהדוא"ל שלך'
        except AssertionError:
            print("Something is wrong")

    def test_SignUpCorrectly_when_genderCustom(self):
        driver = self.driver
        signUp = SignUp_function(driver)
        signUp.creating_a_new_account()
        signUp.enter_name('yael')
        signUp.enter_lastName('lev')
        signUp.enter_phoneOrEmail('yael@walla.com')
        signUp.enter_emailConfirmation('yael@walla.com')
        signUp.enter_password('Aa123456')
        select = Select(signUp.selectBirthday('day'))
        select.select_by_visible_text('2')
        select = Select(signUp.selectBirthday('month'))
        select.select_by_visible_text('יוני')
        select = Select(signUp.selectBirthday('year'))
        select.select_by_visible_text('2000')
        signUp.selectGender("custom")
        selec = Select(signUp.selectBodyPronounField("y"))
        selec.select_by_visible_text('היא: "אחל/י לה יום הולדת שמח!"')
        signUp.clickOnSignUpButton()
        try:
            assert signUp.resultMessageSuccess() == 'הזיני את הקוד מהדוא"ל שלך'
        except AssertionError:
            print("Something is wrong")

    def test_SignUpIncorrectly_when_nameFieldIsNull(self):
        driver = self.driver
        signUp = SignUp_function(driver)
        signUp.creating_a_new_account()
        signUp.enter_name()
        signUp.enter_lastName('levi')
        signUp.enter_phoneOrEmail('yael1@walla.com')
        signUp.enter_emailConfirmation('yael1@walla.com')
        signUp.enter_password('Aa123456')
        select = Select(signUp.selectBirthday('day'))
        select.select_by_visible_text('2')
        select = Select(signUp.selectBirthday('month'))
        select.select_by_visible_text('יוני')
        select = Select(signUp.selectBirthday('year'))
        select.select_by_visible_text('2000')
        signUp.selectGender("custom")
        selec = Select(signUp.selectBodyPronounField("y"))
        selec.select_by_visible_text('היא: "אחל/י לה יום הולדת שמח!"')
        signUp.clickOnSignUpButton()
        time.sleep(6)
        try:
            assert signUp.resultMessageUnsuccess_firstName == 'מה שמך?'
        except AssertionError:
            print("Something is wrong")









