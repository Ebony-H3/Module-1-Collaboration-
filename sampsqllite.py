#For the next example, let’s make a database called enterprise.db and the table zoo to manage our thriving roadside petting zoo business. The table columns are as follows:

#critter-A variable length string, and our primary key.

#count-An integer count of our current inventory for this animal.

#damages-The dollar amount of our current losses from animal–human interactions.

import sqlite3
conn = sqlite3.connect('enterprise.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE zoo
    (critter VARCHAR(20) PRIMARY KEY,
     count INT,
     damages FLOAT)''')
<sqlite3.Cursor object at 0x1006a22d0>

curs.execute('INSERT INTO zoo VALUES("duck", 5, 0.0)')
<sqlite3.Cursor object at 0x1006a22d0>
curs.execute('INSERT INTO zoo VALUES("bear", 2, 1000.0)')
<sqlite3.Cursor object at 0x1006a22d0>