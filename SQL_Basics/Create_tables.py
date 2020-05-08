import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()
# Create Tables
c.execute('''CREATE TABLE stocks2 
                (date text, trans text, symbol text, qty real, price real)''')

conn.commit()
conn.close()
