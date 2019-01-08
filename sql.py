import sqlite3

with sqlite3.connect("sample.db") as connection:
    c = connection.cursor()
    #c.execute("""DROP TABLE posts""")
    c.execute("""CREATE TABLE posts(username TEXT, password TEXT)""")
    c.execute('INSERT INTO posts VALUES("admin", "admin")')