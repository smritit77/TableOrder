from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LogPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.username_locator = ("xpath", '//*[@id="login_email"]')
        self.driver.password_locator = ("xpath",'//*[@id="login_password"]')
        self.driver.login_button_locator = ("xpath",'(//button[normalize-space()="Login"])[1]')
    def open_page(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.driver.find_element(*self.driver.username_locator).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.driver.password_locator).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.driver.login_button_locator).click()