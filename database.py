import sqlite3

# Connect to SQLite database (creates 'store.db' if not exists)
conn = sqlite3.connect('store.db')

# Create a cursor to interact with the database
cursor = conn.cursor()

# Create products table
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL
)
''')

# Create categories table
cursor.execute('''
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)
''')

# Commit changes and close the connection
conn.commit()
conn.close()
print("Database and tables created successfully!")
