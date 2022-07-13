import random
import string
import webdriver_manager


class Utils:
    def __init__(self, driver: webdriver_manager):
        self.driver = driver

    def randomString(self):
        letters = string.ascii_letters
        x = ''.join(random.choice(letters)for i in range(10))
        return x
