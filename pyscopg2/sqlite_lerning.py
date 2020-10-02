import psycopg2

def create_table():
    conn = psycopg2.connect("dbname='database1' user= 'postgres' password = 'fosatti' host= 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTs store(item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insurt(item,quantity,price):
    conn = psycopg2.connect("dbname='database1' user= 'postgres' password = 'fosatti' host= 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES('%s' ,'%s' ,'%s' )" % (item,quantity,price))
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect("dbname='database1' user= 'postgres' password = 'fosatti' host= 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows 

def delete(item):
    conn = psycopg2.connect("dbname='database1' user= 'postgres' password = 'fosatti' host= 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()

def uploade(quantity,item,price):
    conn = psycopg2.connect("dbname='database1' user= 'postgres' password = 'fosatti' host= 'localhost' port = '5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, item=? WHERE price=?",(quantity,item,price))
    conn.commit()
    conn.close()

create_table()
#insurt("banana", 18, 4.79)
#print(view())
#uploade(27, "Chocolate", 5.59)
#delete("Coffe Cup")
