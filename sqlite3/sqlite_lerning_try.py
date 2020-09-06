import sqlite3

def create_table(names ,ages, lastname, networth):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTs database(names TEXT, ages INTIGER, lastname TEXT, networth REAL)")
    cur.execute("INSERT INTO database VALUES(?,?,?,?)",(names,ages,lastname,networth))
    conn.commit()
    conn.close()

name = input("write your first name : ")
age = input("write your age : ")
last_name = input("write your last name : ")
networth = input("write your networth : ")

create_table(name , age, last_name, networth)

def view():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM database")
    rows = cur.fetchall()
    conn.close()
    return rows 

print(view())