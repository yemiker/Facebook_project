import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Web.Base.BasePage import Base
from Web.Pages.Sign_up import SignUp_function
import pytest


@pytest.mark.usefixtures("set_up")
class Test_signUp(Base):
    def test_SignUpCorrectly(self):
        driver = self.driver
        signUp = SignUp_function(driver)
        signUp.creating_a_new_account()
        signUp.enter_name('yael')
        signUp.enter_lastName('lev')
        signUp.enter_phoneOrEmail('123@gamil.com')
        signUp.enter_emailConfirmation('123@gamil.com')
        signUp.enter_password('Aa123456')
        select = Select(signUp.selectBirthday('day'))
        select.select_by_visible_text('2')
        select = Select(signUp.selectBirthday('month'))
        select.select_by_visible_text('יוני')
        select = Select(signUp.selectBirthday('year'))
        select.select_by_visible_text('2000')
        time.sleep(5)









