import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY, 
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

for i in range(1, 10):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f"User{i}", f"example{i}@gmail.com", f"{i * 10}", "1000"))


cursor.execute("UPDATE Users SET balance = ? WHERE id % 2 == 0", (500,))

for i in range(1, 10, 3):
    cursor.execute(f"DELETE FROM Users WHERE id = {i}")

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60 ")
users = cursor.fetchall()
for user in users:
   print(user)


connection.commit()
connection.close()
