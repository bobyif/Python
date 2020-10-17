import sqlite3

class DataBase:

    def __init__(self):
        conn = sqlite3.connect("book.db")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        conn.commit()
        conn.close()

    def insert(self,title, author, year, isbn):
        conn = sqlite3.connect("book.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)" ,(title, author, year, isbn))
        conn.commit()
        conn.close()

    def view(self):
        conn = sqlite3.connect("book.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM book")
        row = cur.fetchall()
        conn.close()
        return row

    def delete(self,id):
        conn = sqlite3.connect("book.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM book WHERE id=?", (id,))
        conn.commit()
        conn.close()

    def search(self, title= "",author= "",year= "",isbn= ""):
        conn = sqlite3.connect("book.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
        row = cur.fetchall()
        conn.close()
        return row

    def update(self, id, title, author, year, isbn):
        conn = sqlite3.connect("book.db")
        cur = conn.cursor()
        cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
        conn.commit()
        conn.close()

#insert("The End", "Jeison Station", 1284, 9342279582)
#delete(2)
#update(3, "The Heist", "Smith Andwester", 1979, 9443269582) 
#print(view())
#print(search(title = "The End"))
#print(search(title = "The End"))
