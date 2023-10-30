import sqlite3
import time
import glob

#TODO: Make first value a key
#TODO: REFACTOR CODE


def printTable():
        #clear console
    print("\033[H\033[J")
    #print the database and table connected to
    print("--------------------------------------------------")
    print(" 📌 DB Connected: " + userChoiceDB + ".db         ")
    print(" 📌 Table Connected: " + userChoiceTable + "         ")
    #print all the tables in the database with their entries
    c = conn.cursor()
    c.execute("""SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;""")
    tables = c.fetchall()
    for table in tables:
        c.execute(f"""SELECT COUNT(*) FROM {table[0]}""")
        entries = c.fetchall()
        print(f" \t ⭕ {table[0]} - {entries[0][0]} entries")
    
    print("--------------------------------------------------")
    print("0. Connect to a different database                ")
    print("1. Connect to a table                             ")
    print("2. Create a new database                          ")
    print("3. Add a new table                                ")
    print("4. Add a new entry(row))                          ")
    print("                                                  ")
    print("5. View all entries(rows)                         ")
    print("                                                  ")
    print("6. Delete a entry(row)                            ")
    print("7. Delete a table                                 ")
    print("8. Delete a database                              ")
    print("                                                  ")
    print("9. Exit                                           ")
    print("--------------------------------------------------")


run = True #whether to run the main loop or not
print("--------------------------------------------------")
print("           Welcome to the DB Manager              ")
print("--------------------------------------------------")
#prints out all of the .db files in the directory with their table
print("📁 | DATABASES FOUND:")
for file in glob.glob("*.db"):
    print(file)
print("--------------------------------------------------")

#user enters database name to connect to
userChoiceDB = input("Enter database you want to connect to: ")
conn = sqlite3.connect(userChoiceDB + ".db")
print("Connecting to database...")
time.sleep(0.2)
print("Connected to database successfully")
time.sleep(0.5)

#ask user to select a table to connect to 
c = conn.cursor()
#print all the tables available in the database
c.execute("""SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;""")
tables = c.fetchall()
print("📁 | TABLES FOUND:")
for table in tables:
    print(table[0])
print("--------------------------------------------------")
userChoiceTable = input("Enter the table you want to connect to: ")


#main loop
while run:
    printTable()
    choice = input("Enter your choice: ")

    while choice not in ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print("Invalid input")
        choice = input("Enter your choice: ")
    #connect to a different database
    if choice == "0":
        conn.close()
        userChoiceDB = input("Enter database you want to connect to: ")
        conn = sqlite3.connect(userChoiceDB + ".db")
        print("Connecting to database...")
        time.sleep(0.2)
        print("Connected to database successfully")
        time.sleep(0.5)
    #connect to a different table
    elif choice == "1":
        c = conn.cursor()
        userChoiceTable = input("Enter the table you want to connect to: ")
        c.execute(f"""SELECT COUNT(*) FROM {userChoiceTable}""")
        entries = c.fetchall()
        print(f"Connected to table {userChoiceTable} successfully")
    #create a new database
    elif choice == "2":
        conn.close()
        userChoiceDB = input("Enter a name for your database: ")
        conn = sqlite3.connect(userChoiceDB + ".db")
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS login (user, pw)""")
        conn.commit()
        print("Database created successfully")
        time.sleep(0.2)
    #add a new table
    elif choice == "3":
        c = conn.cursor()
        c.execute(f"""CREATE TABLE IF NOT EXISTS {userChoiceTable} (user, pw)""")
        conn.commit()
        print("Table created successfully")
        time.sleep(0.2)
    #add a new row
    elif choice == "4":
        c = conn.cursor()
        user = input("Enter the username: ")
        pw = input("Enter the password: ")
        c.execute(f"""INSERT INTO {userChoiceTable} VALUES (?, ?)""", (user, pw))
        conn.commit()
        print("Row added successfully")
        time.sleep(0.2)
    #view all rows
    elif choice == "5":
        conn = sqlite3.connect(userChoiceDB + ".db")
        c = conn.cursor()
        #fail safe if table doesnt exits
        try:
            c.execute(f"""SELECT rowid, * FROM {userChoiceTable}""")
            for row in c.fetchall():
                print(row)
        except:
            print("Table does not exist")
            time.sleep(0.2)
            continue
        conn.commit()
        print("Entries(rows) displayed successfully")
        time.sleep(0.2)
    #delete a row
    elif choice == "6":
        conn = sqlite3.connect(userChoiceDB + ".db")
        c = conn.cursor()
        rowId = input("Enter the row id: ")
        c.execute(f"""DELETE FROM {userChoiceTable} WHERE rowid = {rowId}""") #ERROR: doesnt work for some reason, the row id doesnt exits, also put it in a try except so it doesnt crash
        conn.commit()
        print("Row deleted successfully")
        time.sleep(0.2)
    #delete a table
    elif choice == "7":
        conn = sqlite3.connect(userChoiceDB + ".db")
        c = conn.cursor()
        c.execute(f"""DROP TABLE {userChoiceTable}""")
        conn.commit()
        print("Table deleted successfully")
        time.sleep(0.2)
    #delete a database
    elif choice == "8":
        userChoiceDB = input("Enter the name of the database: ")
        conn = sqlite3.connect(userChoiceDB + ".db")
        c = conn.cursor()
        c.execute(f"""DROP DATABASE {userChoiceDB}""")
        conn.commit()
        conn.close()
        print("Database deleted successfully")  
        time.sleep(0.2)
    #exit
    elif choice == "9":
        conn.close()
        print(f"Exiting...")
        time.sleep(0.2)
        exit()  
    else:
        print("Invalid input")
        time.sleep(0.2)
