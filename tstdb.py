import sqlite3

con = sqlite3.connect('test.db')
cur = con.cursor()
userList = []
#Creating Table
cur.execute("""CREATE TABLE IF NOT EXISTS login 
            (user text PRIMARY KEY, pw integer)""")

#Adding values
cur.execute('''INSERT OR IGNORE INTO login VALUES 
            ('PAR25', '123456')''')

for row in cur.execute('SELECT * FROM login'):
    print(row)

# #Turning Into List
# cur.executemany('INSERT INTO login VALUES (?, ?)', userList)
for row in cur.execute('SELECT * FROM login'):
    userList.append(row)
    
con.commit()
print(userList)


con.close()