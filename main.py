"""
This Program Test My Capabilities in Selenium WebDriver
"""
from selenium import webdriver


# Make a global Config Function that do all the config stuff
def Config():
    pathToWebdriver = r"C:\Users\mouqorra\PycharmProjects\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=pathToWebdriver)
    #requests
    driver.get('https:\\maweb.ma')

Config()
