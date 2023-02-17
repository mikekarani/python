import sqlite3
conn=sqlite3.connect('Mit-midmorning.db')
print("open database successfully")
conn.execute("CREATE TABLE Wanafunzi ("
             "ID INT PRIMARY KEY NULL,"
             "NAME TEXT NOT NULL,"
             "AGE INT NOT NULL,"
             "SCHOOL TEXT NOT NULL,"
             "GENDER TEXT NOT NULL)")
print("tables created successfully")
conn.close()