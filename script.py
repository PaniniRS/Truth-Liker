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


def loginSite(user, pw):
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

# Options                  
# Database active or not
dbActive = False
# Main function
if __name__ == "__main__":
    #Not using a database
    if dbActive == False:
        print("❌ | ERROR: NO DATABASE ACTIVE")
        time.sleep(0.1)
        print("⌛ | STARTING")
        time.sleep(0.2)

        user = input("Enter your username: ")
        pw = input("Enter your password: ")
        post = input("Enter the post you want to like: ")

        loginSite(user=user, pw=pw)
        likePost2(post=post)
        print("✅ | DONE")
        driver.quit()
        exit()
    #Using a database
    else:
        print("✅ | DATABASE ACTIVE")
        time.sleep(0.1)
        print("⌛ | STARTING")
        time.sleep(0.2)
        #for every entry in database login, like the post then log out 
        conn = sqlite3.connect('truthLogins.db')
        c = conn.cursor()
        c.execute("SELECT * FROM login")
        logins = c.fetchall()
        for login in logins:
            loginSite(user=login[0], pw=login[1])
            likePost(post=post)
            driver.get("https://truthsocial.com/logout")
            time.sleep(3)
        conn.close()
