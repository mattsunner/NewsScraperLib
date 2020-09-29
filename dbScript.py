import sqlite3 

conn = sqlite3.connect('headlineData.db')

c = conn.cursor()

c.execute('''CREATE TABLE headlines
             (date text, headline text, url text)''')

conn.commit()
conn.close()