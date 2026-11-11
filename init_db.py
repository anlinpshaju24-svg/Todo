import sqlite3
conn = sqlite3.connect('todos.db')

cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS todos(id INTEGER PRIMARY KEY AUTOINCREMENT,task TEXT NOT NULL )""")
seed = ['Learn Flask', 'Learn SQL', 'Build a project']
for task in seed:
 cursor.execute("INSERT INTO todos(task) VALUES (?)", (task,))
conn.commit()
conn.close()
print("Database ready.")
