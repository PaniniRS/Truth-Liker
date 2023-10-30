import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sqlite3

#test
import glob #for finding all the .db files in the same directory
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# selenium 4
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

#Delete the selenium folder in temp
# import os
# import shutil
# try:
#     shutil.rmtree(os.path.join(os.environ["TMP"], "selenium"), ignore_errors=True)
#     print("✅ | DELETED TEMP SELENIUM FOLDER")
# except:
#     print("❌ | ERROR DELETING TEMP SELENIUM FOLDER")
#     pass


# Edge
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
#Make driver fullscreen
driver.maximize_window()

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
    time.sleep(2.5)
    try:
        #Wait for the button to be able to be clicked
        like = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='Post__actions']//button[@aria-label='Like']"))
)
        # like = driver.find_elementdriver.find_element("xpath", "//div[@class='Post__actions']//button[@aria-label='Like']")
        print(like)
        like.click()
        print("✅ | LIKED POST")
        time.sleep(1)
    except:
        print("❌ | ERROR LIKING POST")
        driver.get(post)

# Options                  
# Database active or not
dbActive = True
# Main function
if __name__ == "__main__":
    #Not using a database
    post = input("Enter the post you want to like: ")
    if dbActive == False:
        print("❌ | ERROR: NO DATABASE ACTIVE")
        time.sleep(0.1)
        print("⌛ | STARTING")
        time.sleep(0.2)
    #Ask for login info and post with a popup
        user = input("Enter your username: ")
        pw = input("Enter your password: ")

        loginSite(user=user, pw=pw)
        likePost(post=post)
        print("✅ | DONE")
        driver.quit()
        exit()
    #Using a database
    else:
        print("📌 | DATABASE MODE ACTIVE")
        #print all the .db files found in the same directory
        print("📁 | DATABASES FOUND:")
        for file in glob.glob("*.db"):
            print(file)
        #print the tables found in each of the databases
        print("📁 | TABLES FOUND:")
        for file in glob.glob("*.db"):
            conn = sqlite3.connect(file)
            c = conn.cursor()
            c.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = c.fetchall()
            for table in tables:
                print(table[0])
            conn.close()
        #ask for the database name and table name
        database = input("Enter the database name: ")
        table = input("Enter the table name: ")

        time.sleep(0.3)
        print("⌛ | STARTING")
        time.sleep(0.4)
        #for every entry in database login, like the post then log out 
        conn = sqlite3.connect(f'{database}.db')
        print(f"✅ | DATABASE CONNECTED")
        c = conn.cursor()
        c.execute(f"SELECT * FROM {table}") #TODO: make this adaptable normal is the table name, ask the user
        logins = c.fetchall()
        for login in logins:
            loginSite(user=login[0], pw=login[1])
            likePost(post=post)
            driver.get("https://truthsocial.com/logout")
            time.sleep(3)
        conn.close()
