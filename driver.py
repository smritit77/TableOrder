from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class sajhamenu:
    def driverlogin(self):
        profile_directory = "C:\\Users\\Hp\\AppData\\Local\\Google\\Chrome\\User Data"

        options = webdriver.ChromeOptions()
        options.add_argument(f"--user-data-dir={profile_directory}")
        options.add_argument('--profile-directory=Default')

        driver=webdriver.Chrome(options=options)
        sleep(5)
        driver.get("https://testh.tunahms.com/sajha_menu")
        sleep(5)
        driver.maximize_window()
        return driver