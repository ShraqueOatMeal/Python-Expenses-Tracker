import sqlite3

#connect to database
conn = sqlite3.connect("expenses.db")

cur = conn.cursor()

cur.execute("""create table expenses
(id integer primary key, 
Date date,
Description nvarchar(50),
Category nvarchar(50),
Price decimal(10, 2))""")

conn.commit()
conn.close()