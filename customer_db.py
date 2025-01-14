import sqlite3

connection = sqlite3.connect("customer.db")
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Customer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fname TEXT NOT NULL,
    lname TEXT NOT NULL,
    address TEXT NOT NULL, 
    mobile TEXT NOT NULL)
    """)
connection.commit()

cursor.execute("""
INSERT INTO Customer (fname, lname, address, mobile) VALUES
        ('Amnon', 'Mizrachi', '39 Hatmarim st. Eilat', '052-5571136'),
        ('Gonen', 'David', 'Harav Nissim 12 Ramat Gan', '051-5331792'),
        ('Sima', 'Shushan', 'Bnei Moshe 53 Bnei Brak', '055-5315240')    
    """)


connection.commit()




