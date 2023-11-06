import sqlite3
import datetime

now = datetime.datetime.utcnow()

CREATE_GROCERIES = "CREATE TABLE IF NOT EXISTS groceries (id INTEGER PRIMARY KEY,name TEXT,price INTEGER,date DATE);"
CREATE_TRANSPORTATION = "CREATE TABLE IF NOT EXISTS transportation (id INTEGER PRIMARY KEY,name TEXT,price INTEGER,date DATE);"
CREATE_ENTERTAINMENT = "CREATE TABLE IF NOT EXISTS entertainment (id INTEGER PRIMARY KEY,name TEXT,price INTEGER,date DATE);"
CREATE_UTILITIES = "CREATE TABLE IF NOT EXISTS utilities (id INTEGER PRIMARY KEY,name TEXT,price INTEGER,date DATE);"
CREATE_OTHER = "CREATE TABLE IF NOT EXISTS other (id INTEGER PRIMARY KEY,name TEXT,price INTEGER,date DATE);"

INSERT_GROCERIES = "INSERT INTO groceries (name,price,date) VALUES(?, ?, ?);"
INSERT_TRANSPORTATION = "INSERT INTO transportation (name,price,date) VALUES(?, ?, ?);"
INSERT_ENTERTAINMENT = "INSERT INTO entertainment (name,price,date) VALUES(?, ?, ?);"
INSERT_UTILITIES = "INSERT INTO utilities (name,price,date) VALUES(?, ?, ?);"
INSERT_OTHER = "INSERT INTO other (name,price,date) VALUES(?, ?, ?);"

SELECT_ALL1 = "SELECT * FROM  groceries;"
SELECT_ALL2 = "SELECT * FROM  transportation;"
SELECT_ALL3 = "SELECT * FROM  entertainment;"
SELECT_ALL4 = "SELECT * FROM  utilities;"
SELECT_ALL4 = "SELECT * FROM  other;"

SELECT_GROCERIES = "SELECT * FROM groceries WHERE name = ? AND price = ?;"
SELECT_TRANSPORTATION = "SELECT * FROM transportation WHERE name = ? AND price = ?;"
SELECT_ENTERTAINMENT = "SELECT * FROM entertainment WHERE name = ? AND price = ?;"
SELECT_UTILITIES = "SELECT * FROM utilities WHERE name = ? AND price = ?;"
SELECT_OTHER = "SELECT * FROM other WHERE name = ? AND price = ?;"

DELETE_GROCERIES = "DELETE FROM groceries WHERE name = ? AND price = ?;"
DELETE_TRANSPORTATION  = "DELETE FROM transportation WHERE name = ? AND price = ?;"
DELETE_ENTERTAINMENT= "DELETE FROM entertainment WHERE name = ? AND price = ?;"
DELETE_UTILITIES = "DELETE FROM utilities WHERE name = ? AND price = ?;"
DELETE_OTHER = "DELETE FROM other WHERE name = ? AND price = ?;"

tables_list = [CREATE_GROCERIES,CREATE_TRANSPORTATION,CREATE_ENTERTAINMENT,CREATE_UTILITIES,CREATE_OTHER]

def create_tables():
    conn = sqlite3.connect('expenses.db')
    with conn:
        for table in tables_list:
            conn.execute(table)


