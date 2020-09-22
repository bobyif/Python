import psycopg2

def create_table():
    conn = psycopg2.connect("dbname= 'database1' user= 'postgres' password= 'fosatti' host = 'localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTIGER, price REAL)")
    conn.commit()
    conn.close()

def insurt(item,quantity,price):
    conn = psycopg2.connect("lite.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows 

def delete(item):
    conn = psycopg2.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()

def uploade(quantity,item,price):
    conn = psycopg2.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, item=? WHERE price=?",(quantity,item,price))
    conn.commit()
    conn.close()

create_table()
uploade(27, "Chocolate", 5.59)
#delete("Coffe Cup")
#print(view())
#create_table("cake", 18, 4.79)