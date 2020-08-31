import sqlite3

    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTIGER, price REAL)")
    cur.execute("INSERT INTO store VALUES ('Wine Glass', 8, 10.9)")
    conn.commit()
    conn.close()