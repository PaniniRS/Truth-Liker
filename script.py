import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sqlite3

# selenium 4
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# open the driver in full screen
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--allow-running-insecure-content")

# Edge
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)

def loginSite(user, pw):
    try:
        driver.get("https://truthsocial.com/login")
        time.sleep(3)
        appendLoginUsername = driver.find_element("name", "username")
        appendLoginUsername.send_keys(user)
        appendLoginPassword = driver.find_element("name", "password")
        appendLoginPassword.send_keys(pw)
        time.sleep(1)
        appendLoginPassword.send_keys(Keys.ENTER)
        time.sleep(3)
        print(f"✅ | LOGGED IN WITH {user}");
    except:
        print("❌ | ERROR LOGGING IN")
        driver.quit()

def likePost(post):
    driver.get(post)
    try:
        like = driver.find_element("xpath", "//span[normalize-space()='Like']")
        like.click()
        time.sleep(1)
    except:
        print("❌ | ERROR LIKING POST")
        driver.get(post)
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
    #Ask for login info and post with a popup
        user = input("Enter your username: ")
        pw = input("Enter your password: ")
        post = input("Enter the post you want to like: ")

        loginSite(user=user, pw=pw)
        likePost(post=post)
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
