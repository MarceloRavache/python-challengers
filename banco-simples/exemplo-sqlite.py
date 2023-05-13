import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()
cursor.execute('''CREATE TABLE clientes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    idade INTEGER,
                    email TEXT
                )''')
cursor.execute("INSERT INTO clientes (nome, idade, email) VALUES (?, ?, ?)", ('João', 25, 'joao@example.com'))
cursor.execute("INSERT INTO clientes (nome, idade, email) VALUES (?, ?, ?)", ('Maria', 30, 'maria@example.com'))
cursor.execute("SELECT * FROM clientes")
clientes = cursor.fetchall()
for cliente in clientes:
    print(cliente)

conn.close()