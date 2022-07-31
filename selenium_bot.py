from bs4 import BeautifulSoup as bs
import selenium.common.exceptions
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

 



def path(): 
    global chrome
    # print("enter the driver path")
    # exe_path = input()
    exe_path = "/Users/magi-nerv/Desktop/chromedriver"
    # starts a new chrome session
    chrome = webdriver.Chrome(executable_path = exe_path)


def url_name(url): 
    # the web page opens up
    chrome.get(url)
    # Instagram: https://www.instagram.com/accounts/login/

    # webdriver will wait for 4 sec before throwing a 
    # NoSuchElement exception so that the element
    # is detected and not skipped.
    time.sleep(4)

def login():

    print("enter username")
    username = input()
    

    print("enter password")
    your_password = input()

    # finds the username box
    usern = chrome.find_element(By.NAME,"username")

    # sends the entered username
    usern.send_keys(username)

    # finds the password box
    passw = chrome.find_element(By.NAME,"password")

    # sends the entered password
    passw.send_keys(your_password)    
    passw.send_keys(Keys.RETURN)
    time.sleep(4)

    
    # notn = chrome.find_element_by_class_name("yWX7d")# dont save info button
    # notn.click()# click don't save button

    # time.sleep(1)

    # finds the login button
    # log_but = chrome.find_element(By.CLASS_NAME,"L3NKy")
    # time.sleep(2)

    # # clicks the login button
    # log_but.click()
    # time.sleep(4)

    code_box = chrome.find_element(By.NAME,"verificationCode")
    print("enter verification code (no spaces):")
    code = input()
    code_box.send_keys(code)

    code_box.send_keys(Keys.RETURN)

    
    







# Starts code down here


urls = {"Instagram Login": "https://www.instagram.com/accounts/login/","model": "Mustang","year": 1964}
print("What do i do?")
response = input()
while (response != "quit"):


    if response == "setup":
        path()
        print("setting up chrome")
    
    # Goes to URL
    if response == "url": 
        print("Where would you like to go?")
        print(urls)
        
        response = input()
        if response in urls:
            url_name(urls[response])
        else:
            print("URL NOT IN SHEET")

    if response == "login":
        login()
    

    if response == "login insta":
        path()
        url_name(urls["Instagram Login"])
        login()
    
    print("What do i do?")
    response = input()
