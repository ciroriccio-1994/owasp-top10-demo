# sql_injection_fixed.py
# Example of a secure SQL query (parameterized, safe from SQL Injection)

import sqlite3

def bootstrap_db(conn):
    cur = conn.cursor()
    cur.execute("CREATE TABLE users (name TEXT, password TEXT)")
    cur.executemany("INSERT INTO users VALUES (?, ?)", [("alice", "alice123"), ("bob", "hunter2")])
    conn.commit()

def main():
    conn = sqlite3.connect(":memory:")
    bootstrap_db(conn)
    cur = conn.cursor()

    print("== Secure Login Demo ==")
    username = input("Enter username: ")
    password = input("Enter password: ")

    # ✅ Secure query (parameterized)
    query = "SELECT * FROM users WHERE name = ? AND password = ?"
    print(f"[DEBUG] Executing: {query} with params ({username}, {password})")

    cur.execute(query, (username, password))
    result = cur.fetchone()

    if result:
        print(f"Welcome {result[0]}!")
    else:
        print("Login failed.")

if __name__ == "__main__":
    main()
