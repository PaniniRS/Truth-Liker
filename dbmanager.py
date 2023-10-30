import sqlite3
import time
import glob

#TODO: Make first value a key

run = True
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

#main loop
while run:
    print("--------------------------------------------------")
    print(" 📌 DB Connected: " + userChoiceDB + ".db         ")
    #display tables in connected database and the number of entries they have
    c = conn.cursor()
    c.execute("""SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;""")
    tables = c.fetchall()
    for table in tables:
        c.execute(f"""SELECT COUNT(*) FROM {table[0]}""")
        entries = c.fetchall()
        print(f" ⭕ {table[0]} - {entries[0][0]} entries")
    print("                                                  ")
    print("--------------------------------------------------")
    print("0. Connect to a different database                ")
    print("1. Create a new database                          ")
    print("2. Add a new table                                ")
    print("3. Add a new entry(row))                          ")
    print("                                                  ")
    print("4. View all entries(rows)                         ")
    print("                                                  ")
    print("5. Delete a entry(row)                            ")
    print("6. Delete a table                                 ")
    print("7. Delete a database                              ")
    print("                                                  ")
    print("8. Exit                                           ")
    print("--------------------------------------------------")

    choice = input("Enter your choice: ")

    while choice not in ["0","1", "2", "3", "4", "5", "6", "7", "8"]:
        print("Invalid input")
        choice = input("Enter your choice: ")
    if choice == "0":
        #connect to a different database
        conn.close()
        userChoiceDB = input("Enter database you want to connect to: ")
        conn = sqlite3.connect(userChoiceDB + ".db")
        print("Connecting to database...")
        time.sleep(0.2)
        print("Connected to database successfully")
        time.sleep(0.5)
    elif choice == "1":
        #create a new database
        conn.close()
        userChoiceDB = input("Enter a name for your database: ")
        conn = sqlite3.connect(userChoiceDB + ".db")
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS login (user, pw)""")
        conn.commit()
        print("Database created successfully")
        time.sleep(0.2)
    elif choice == "2":
        #add a new table
        c = conn.cursor()
        tableName = input("Enter a name for your table: ") #TODO: make it so you only selec it once so you dont have to ask every time and repeat code
        c.execute(f"""CREATE TABLE IF NOT EXISTS {tableName} (user, pw)""")
        conn.commit()
        print("Table created successfully")
        time.sleep(0.2)
    elif choice == "3":
        #add a new row
        c = conn.cursor()
        tableName = input("Enter the name of the table: ")
        user = input("Enter the username: ")
        pw = input("Enter the password: ")
        c.execute(f"""INSERT INTO {tableName} VALUES (?, ?)""", (user, pw))
        conn.commit()
        print("Row added successfully")
        time.sleep(0.2)
    elif choice == "4":
        #view all rows
        conn = sqlite3.connect(userChoiceDB + ".db")
        c = conn.cursor()
        tableName = input("Enter the name of the table: ")
        #fail safe if table doesnt exits
        try:
            c.execute(f"""SELECT rowid, * FROM {tableName}""")
            for row in c.fetchall():
                print(row)
        except:
            print("Table does not exist")
            time.sleep(0.2)
            continue
        conn.commit()
        print("Entries(rows) displayed successfully")
        time.sleep(0.2)
    elif choice == "5":
        #delete a row
        conn = sqlite3.connect(userChoiceDB + ".db")
        c = conn.cursor()
        tableName = input("Enter the name of the table: ")
        rowId = input("Enter the row id: ")
        c.execute(f"""DELETE FROM {tableName} WHERE rowid = {rowId}""") #ERROR: doesnt work for some reason, the row id doesnt exits, also put it in a try except so it doesnt crash
        conn.commit()
        print("Row deleted successfully")
        time.sleep(0.2)
    elif choice == "6":
        #delete a table
        conn = sqlite3.connect(userChoiceDB + ".db")
        c = conn.cursor()
        tableName = input("Enter the name of the table: ")
        c.execute(f"""DROP TABLE {tableName}""")
        conn.commit()
        print("Table deleted successfully")
        time.sleep(0.2)
    elif choice == "7":
        #delete a database
        userChoiceDB = input("Enter the name of the database: ")
        conn = sqlite3.connect(userChoiceDB + ".db")
        c = conn.cursor()
        c.execute(f"""DROP DATABASE {userChoiceDB}""")
        conn.commit()
        conn.close()
        print("Database deleted successfully")  
        time.sleep(0.2)
    elif choice == "8":
        #exit
        conn.close()
        print(f"Exiting...")
        time.sleep(0.2)
        exit()  
    else:
        print("Invalid input")
        time.sleep(0.2)
