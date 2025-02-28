import sqlite3

conn = sqlite3.connect('notes.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL
)
''')

conn.commit()
conn.close()

