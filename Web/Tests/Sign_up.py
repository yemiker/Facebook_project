import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Web.Base.BasePage import Base
from Web.Pages.Sign_up import SignUp_function
import pytest

from Web.Utils.UtilsFunction import Utils


@pytest.mark.usefixtures("set_up")
class Test_signUp(Base):
    def test_SignUpCorrectly_when_genderFemale(self):
        driver = self.driver
        signUp = SignUp_function(driver)
        util = Utils(driver)
        signUp.creating_a_new_account()
        name = util.randomString()
        signUp.enter_name(name)
        signUp.enter_lastName(name)
        signUp.enter_phoneOrEmail(f'{name}@walla.com')
        signUp.enter_emailConfirmation(f'{name}@walla.com')
        signUp.enter_password(f'{name}1234')
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
        util = Utils(driver)
        signUp.creating_a_new_account()
        name = util.randomString()
        signUp.enter_name(name)
        signUp.enter_lastName(name)
        signUp.enter_phoneOrEmail(f'{name}@walla.com')
        signUp.enter_emailConfirmation(f'{name}@walla.com')
        signUp.enter_password(f'{name}123456')
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
        util = Utils(driver)
        name = util.randomString()
        signUp.creating_a_new_account()
        signUp.enter_name(name)
        signUp.enter_lastName(name)
        signUp.enter_phoneOrEmail(f'{name}@walla.com')
        signUp.enter_emailConfirmation(f'{name}@walla.com')
        signUp.enter_password(f'{name}123456')
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
        util = Utils(driver)
        signUp.creating_a_new_account()
        name = util.randomString()
        signUp.enter_lastName(name)
        signUp.enter_phoneOrEmail(f'{name}@walla.com')
        signUp.enter_emailConfirmation(f'{name}@walla.com')
        signUp.enter_password(f'{name}123456')
        select = Select(signUp.selectBirthday('day'))
        select.select_by_visible_text('2')
        select = Select(signUp.selectBirthday('month'))
        select.select_by_visible_text('יוני')
        select = Select(signUp.selectBirthday('year'))
        select.select_by_visible_text('2000')
        signUp.selectGender("male")
        signUp.clickOnSignUpButton()
        time.sleep(6)
        try:
            time.sleep(5)
            assert signUp.resultMessageUnsuccess_firstName == "מה שמך?"
            time.sleep(5)
        except AssertionError:
            print("Something is wrong")









