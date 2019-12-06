from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import unittest
import time

#change these to match your setting
DRIVER_PATH = "C:/Chrome driver/chromedriver.exe"
BROWSER_PATH = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe"
USERNAME = "a"
PASSWORD = "a"

class test_playthrough(unittest.TestCase):

    def set_up(self,driver_path,browser_path):
        """
        set up  browser with custom driver and browser path
        """

        option = webdriver.ChromeOptions()
        option.binary_location = browser_path
        browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
        return browser

    def test_play_through(self):

        browser_host = self.set_up(DRIVER_PATH,BROWSER_PATH)
        browser_host.get("http://localhost:8000/admin")
        username_field = browser_host.find_element_by_name("username")
        username_field.send_keys(USERNAME)
        password_field = browser_host.find_element_by_name("password")
        password_field.send_keys(PASSWORD)
        password_field.send_keys(Keys.ENTER)
        browser_host.get("http://localhost:8000/")
        element = browser_host.find_element_by_name("login_button")
        element.click()
        self.assertEqual(browser_host.current_url,"http://localhost:8000/login/")
        element = browser_host.find_element_by_name("create_room")
        element.click()
        self.assertEqual(browser_host.current_url,"http://localhost:8000/login/host/")
        browser_host.close()

