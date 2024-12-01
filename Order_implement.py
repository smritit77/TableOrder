from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from subprocess import call
from selenium.webdriver.common.action_chains import ActionChains
# from Order_locator import orderlocator

class TableOrder():
    from Order_locator import orderlocator

    def __init__(self, driver):
        self.driver = driver

    def selectable_table(self):
        self.driver.find_element(*self.orderlocator.select_table).click()

    def clickable_makeorder(self):
        self.driver.find_element(*self.orderlocator.click_makeorder).click()

    def clickable_itemcategory(self):
        self.driver.find_element(*self.orderlocator.click_itemcategory).click()

    def selectable_item(self):
        self.driver.find_element(*self.orderlocator.select_item1).click()
        self.driver.find_element(*self.orderlocator.select_item2).click()

    def clickable_placeorder(self):
        self.driver.find_element(*self.orderlocator.click_placeorder).click()

    def clickable_customerfield(self):
        self.driver.find_element(*self.orderlocator.click_customerfield).send_keys("Smriti Thapa")
        self.driver.find_element(*self.orderlocator.click_smriti).click()