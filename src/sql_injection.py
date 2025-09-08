# sql_injection.py
# Example of an insecure SQL query (vulnerable to SQL Injection)

import sqlite3

# Create in-memory DB with test users
conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("CREATE TABLE users (name TEXT, password TEXT)")
cur.executemany("INSERT INTO users VALUES (?, ?)", [("alice", "alice123"), ("bob", "hunter2")])
conn.commit()

# Get input from user
username = input("Enter username: ")
password = input("Enter password: ")

# ❌ Vulnerable query (string concatenation)
query = f"SELECT * FROM users WHERE name = '{username}' AND password = '{password}'"
print(f"[DEBUG] Executing: {query}")

cur.execute(query)
result = cur.fetchone()

if result:
    print(f"Welcome {result[0]}!")
else:
    print("Login failed.")
