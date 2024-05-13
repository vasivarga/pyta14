from selenium import webdriver


class Browser:

    def __init__(self):
        self.driver = None

    def start(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def close(self):
        self.driver.close()