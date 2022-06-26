from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager


class Base:

    @pytest.fixture(autouse=True)
    def set_up(self):
        print("Initiating Chrome driver")
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        print("-----------------------------------------")
        print("Test is started")
        self.driver.implicitly_wait(10)
        self.driver.get("https://he-il.facebook.com/")
        self.driver.maximize_window()
        yield self.driver
        if self.driver is not None:
            print("-----------------------------------------")
            print("Tests is finished")
            self.driver.close()
            self.driver.quit()
