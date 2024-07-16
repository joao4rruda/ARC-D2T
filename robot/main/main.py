from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

from robot.api import News

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

func_News = News();

def main():

    api_link = "https://newsapi.org/v2/everything?"
    api_key = "80423fcb354f45ea8fb17e14b61fc04a"

    News.get_news(api_link, api_key);

    