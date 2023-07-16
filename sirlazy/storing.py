import sqlite3

DB_NAME = "sirlazy.db"

con = sqlite3.connect(DB_NAME)

cur = con.cursor()

