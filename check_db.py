import sqlite3

db = sqlite3.connect("planner.db")
cursor = db.cursor()

cursor.execute("SELECT id, username, email FROM users")

print(cursor.fetchall())

db.close()