"""
This Program Test My Capabilities in Selenium WebDriver
"""
from selenium import webdriver

import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def check(email):
    if (re.search(regex, email)):
        print("Valid Email")
    else:
        print("Invalid Email")


if __name__ == '__main__':
    email = "rohit.gupta@mcnsolutions.net"
    check(email)

    email = "praveen@c-sharpcorner.com"
    check(email)

    email = "inform2atul@gmail.com"
    check(email)
# Make a global Config Function that do all the config stuff
def Config():
    pathToWebdriver = r"C:\Users\mouqorra\PycharmProjects\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=pathToWebdriver)
    #requests
    driver.get('https:\\maweb.ma')

Config()
