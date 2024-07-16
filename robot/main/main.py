from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def get_driver():

    options = webdriver.ChromeOptions()

    options.add_argument(
        "disable-maxized"
    )

    options.add_argument(
        'disable-dev-shm-usage'
    )

    options.add_argument("no-sandbox")

    options.add_experimental_option(
        "excludeSwitches", ["enable-automation"]
    )

    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options)

    driver.get("ttp://automated.pythonanywhere.com/login/")
    return driver