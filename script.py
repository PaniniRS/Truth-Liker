import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sqlite3
import os

# selenium 4
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

# LOGIN DB
conn = sqlite3.connect('login.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS login (user, pw)""")
conn.commit()
conn.close()

user = "lindaholt1995@outlook.com"
pw = "Juventus12"
post = input("LINK OD POSTOT: ")


# LOGIN


browser.get(post)
time.sleep(3)

def login(user, pw):
    try:
        browser.get("https://truthsocial.com/login")
        time.sleep(3)
        appendLoginUsername = browser.find_element("name", "username")
        appendLoginUsername.send_keys(user)
        appendLoginPassword = browser.find_element("name", "password")
        appendLoginPassword.send_keys(pw)
        time.sleep(1)
        appendLoginPassword.send_keys(Keys.ENTER)
        time.sleep(3)
        print(f"✅ | LOGGED IN WITH {user}");
    except:
        print("❌ | ERROR LOGGING IN")
        browser.quit()

def likePost(post):
    try:
        browser.get(post)
        time.sleep(3)
        likeButton = browser.find_element("xpath", "/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div")
        likeButton.click()
        time.sleep(3)
        print("     | POST LIKED")
    except:
        print("❌ | ERROR LIKING POST")
        browser.quit()

def likePost2(post):
    try:
        like = browser.find_element("xpath", "//span[normalize-space()='Like']")
        like.click()
        time.sleep(1)
    except:
        print("❌ | ERROR LIKING POST")
        browser.get(post)
        time.sleep(3)
                                          

# Main function
if __name__ == "__main__":
    print("⌛ | STARTING")


    login(user=user, pw=pw)
    likePost2(post=post)
    print("✅ | DONE")
    browser.quit()    