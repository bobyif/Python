import sqlite3

class DataBase:

    def __init__(self, db):
        self.conn = sqlite3.connect("book.db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.conn.commit()
        
    def insert(self,title,author,year,isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)" ,(title, author, year, isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        row = self.cur.fetchall()
        return row

    def delete(self,id):
        conn = sqlite3.connect("book.db")
        cur = conn.cursor()a
        cur.execute("DELETE FROM book WHERE id=?", (id,))
        conn.commit()
        conn.close()
    
    def __del__(self):
        self.conn.close()
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()


    def search(self, title= "",author= "",year= "",isbn= ""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
        row = self.cur.fetchall()
        return row

    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
        self.conn.commit()

        self.conn.close()


#insert("The End", "Jeison Station", 1284, 9342279582)
#delete(2)
#update(3, "The Heist", "Smith Andwester", 1979, 9443269582) 
#print(view())
#print(search(title = "The End"))
#print(search(title = "The End"))