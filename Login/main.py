import sqlite3
import hashlib

conn = sqlite3.connect("pet.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS pet (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
""")

username1, password1 = "mike123", hashlib.sha256("mikepassword".encode()).hexdigest()
username2, password2 = "mycat123", hashlib.sha256("mikepassword".encode()).hexdigest()
username3, password3 = "meow123", hashlib.sha256("mikepassword".encode()).hexdigest()
username4, password4 = "r67tyuhjkeedws", hashlib.sha256("mikepassword".encode()).hexdigest()

c.execute("INSERT INTO pet (name, password) VALUES (?, ?)", (username1, password1))
c.execute("INSERT INTO pet (name, password) VALUES (?, ?)", (username2, password2))
c.execute("INSERT INTO pet (name, password) VALUES (?, ?)", (username3, password3))
c.execute("INSERT INTO pet (name, password) VALUES (?, ?)", (username4, password4))

conn.commit()
conn.close()

print("Users inserted successfully!")