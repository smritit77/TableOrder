from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from subprocess import call
from selenium.webdriver.common.action_chains import ActionChains
from Order_locator import orderlocator
from Order_implement import TableOrder

class order:
   #ekchoti login vaisakey pachi feri login huna pardaina
    profile_directory = "C:\\Users\\Hp\\AppData\\Local\\Google\\Chrome\\User Data"

    options = webdriver.ChromeOptions()
    options.add_argument(f"--user-data-dir={profile_directory}")
    options.add_argument('--profile-directory=Default')

    driver=webdriver.Chrome(options=options)
    sleep(5)
    driver.get("https://testh.tunahms.com/sajha_menu")
    sleep(5)

    def Sajha_Menu(driver):
        Make_Order = TableOrder(driver)
        Make_Order.selectable_table()
        sleep(2)
        Make_Order.clickable_makeorder()
        sleep(2)
        Make_Order.clickable_itemcategory()
        sleep(2)
        Make_Order.selectable_item()
        sleep(2)
        # Make_Order.clickable_placeorder()
        # sleep(2)
        # Make_Order.clickable_customerfield()
        # sleep(2)
    Sajha_Menu(driver)