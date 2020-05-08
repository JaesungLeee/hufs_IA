import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()
# Create Tables
c.execute('''CREATE TABLE stocks 
                (date text, trans text, symbol text, qty real, price real)''')


# Many Columns
c.execute("INSERT INTO stocks VALUES (?, ?, ?, ?, ?)",
          ('2006-01-05', 'BUY', 'RHAT', 100, 35.14))

purchase = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
            ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
            ('2006-04-06', 'SELL', 'SAMSUNG', 500, 35.14),
            ]

c.executemany("INSERT INTO stocks VALUES (?, ?, ?, ?, ?)", purchase)

c.execute("SELECT * FROM stocks")  # 모든 column 가져옴
for row in c.fetchall():    # return 되는것을 전부 가져옴
    print(row)
print()

c.execute("SELECT * FROM stocks WHERE symbol = ?", ('RHAT', ))  # symbol이 'RHAT'
print(c.fetchone())
print()

c.execute("UPDATE stocks SET qty = ? WHERE symbol = ?", (700, "MSFT"))
# symbol이 MSFT인데 qty를 700으로 UPDATE

c.execute("DELETE FROM stocks WHERE trans = ?", ("SELL", ))
# trans = SELL인 ROW를 DELETE

c.execute("SELECT * FROM stocks ORDER BY price")    # price기준으로 sorting
for row in c.fetchall():
    print(row)

conn.commit()
conn.close()