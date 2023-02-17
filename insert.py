import sqlite3
conn=sqlite3.connect('Mit-Midmorning.db')
print("opn database successfully")
conn.execute("INSERT INTO Wanafunzi(ID, NAME, AGE, SCHOOL, GENDER)VALUES (1,'ERICK',30,'eMobilis','MALE')")
conn.execute("INSERT INTO Wanafunzi(ID, NAME, AGE, SCHOOL, GENDER)VALUES (2,'SOLOMON',19,'eMobilis','MALE')")
conn.execute("INSERT INTO Wanafunzi(ID, NAME, AGE, SCHOOL, GENDER)VALUES (3,'SUSAN',29,'eMobilis','FEMALE')")
conn.execute("INSERT INTO Wanafunzi(ID, NAME, AGE, SCHOOL, GENDER)VALUES (4,'ISABEL',20,'eMobilis','FEMALE')")
conn.execute("INSERT INTO Wanafunzi(ID, NAME, AGE, SCHOOL, GENDER)VALUES (5,'JOHN',24,'eMobilis','MALE')")
conn.execute("INSERT INTO Wanafunzi(ID, NAME, AGE, SCHOOL, GENDER)VALUES (6,'STEPHEN',35,'eMobilis','MALE')")


conn.commit()
print("Recoddrs added successfully")
conn.close()
