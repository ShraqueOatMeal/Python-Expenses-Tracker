import sqlite3

# connect to database
conn = sqlite3.connect("expenses.db")

cur = conn.cursor()

# check for any errors
cur.execute("PRAGMA table_info(expenses);")
result = cur.fetchall()

print(result)

conn.close()