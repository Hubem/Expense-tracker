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
SELECT_ALL5 = "SELECT * FROM  other;"

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

DELETE_GROCERIES_BY_ID = "DELETE FROM groceries WHERE id = ?;"

tables_list = [CREATE_GROCERIES,CREATE_TRANSPORTATION,CREATE_ENTERTAINMENT,CREATE_UTILITIES,CREATE_OTHER]

def create_tables():
    conn = sqlite3.connect('Adatbazis/expenses.db')
    with conn:
        for table in tables_list:
            conn.execute(table)

#insert functions

def insert_groceries(name, price, date):
    conn=sqlite3.connect('Adatbazis/expenses.db')
    with conn:
        c=conn.cursor()
        c.execute(INSERT_GROCERIES,(name, price, date))
        conn.commit()
    c.close()



def insert_transportation(name, price, date):
    conn=sqlite3.connect('Adatbazis/expenses.db')
    with conn:
        c=conn.cursor()
        c.execute(INSERT_TRANSPORTATION,(name, price, date))
        conn.commit()
        c.close()

def insert_entertainment(name, price, date):
    conn=sqlite3.connect('Adatbazis/expenses.db')
    with conn:
        c=conn.cursor()
        c.execute(INSERT_ENTERTAINMENT,(name, price, date))
        conn.commit()
        c.close()

def insert_utilities(name, price, date):
    conn=sqlite3.connect('Adatbazis/expenses.db')
    with conn:
        c=conn.cursor()
        c.execute(INSERT_UTILITIES,(name, price, date))
        conn.commit()
        c.close()

def insert_other(name, price, date):
    conn=sqlite3.connect('Adatbazis/expenses.db')
    with conn:
        c=conn.cursor()
        c.execute(INSERT_OTHER,(name, price, date))
        conn.commit()
        c.close()


#delete functions

def delete_groceries(good, price):
    conn = sqlite3.connect('Adatbazis/expenses.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_GROCERIES, (good, price))
        conn.commit()
        c.close()

def delete_gro_by_id(id):
    conn = sqlite3.connect('Adatbazis/expenses.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_GROCERIES_BY_ID,(id,))
        conn.commit()
        c.close()


def delete_transportation(good, price):
    conn = sqlite3.connect('Adatbazis/expenses.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_TRANSPORTATION, (good, price))
        conn.commit()
        c.close()


def delete_entertainment(good, price):
    conn = sqlite3.connect('Adatbazis/expenses.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_ENTERTAINMENT, (good, price))
        conn.commit()
        c.close()


def delete_utilities(good, price):
    conn = sqlite3.connect('Adatbazis/expenses.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_UTILITIES, (good, price))
        conn.commit()
        c.close()


def delete_other(good, price):
    conn = sqlite3.connect('Adatbazis/expenses.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_OTHER, (good, price))
        conn.commit()
        c.close()


#select all functions

def select_all_groceries():
    conn = sqlite3.connect('Adatbazis/expenses.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ALL1)
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + str(x[3]) + '\n'
        return output

def select_all_gro():
    conn = sqlite3.connect('Adatbazis/expenses.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ALL1)
        rows = c.fetchall()
        c.close()
        return rows


        

def select_all_transportation():
    conn = sqlite3.connect('Adatbazis/expenses.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ALL2)
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + str(x[3]) + '\n'
        return output
    

def select_all_entertainment():
    conn = sqlite3.connect('Adatbazis/expenses.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ALL3)
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + str(x[3]) + '\n'
        return output
    

def select_all_utilities():
    conn = sqlite3.connect('Adatbazis/expenses.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ALL4)
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + str(x[3]) + '\n'
        return output
    

def select_all_other():
    conn = sqlite3.connect('Adatbazis/expenses.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ALL4)
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + str(x[3]) + '\n'
        return output
    

#select specific funcions

def select_groceries(good, price):
    conn = sqlite3.connect('Adatbazis/expenses.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_GROCERIES, (good, price))
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + str(x[3]) + '\n'
        return output
    

def select_transportation(good, price):
    conn = sqlite3.connect('Adatbazis/expenses.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_TRANSPORTATION, (good, price))
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + str(x[3]) + '\n'
        return output
    

def select_entertainment(good, price):
    conn = sqlite3.connect('Adatbazis/expenses.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ENTERTAINMENT, (good, price))
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + str(x[3]) + '\n'
        return output
    

def select_utilities(good, price):
    conn = sqlite3.connect('Adatbazis/expenses.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_UTILITIES, (good, price))
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + str(x[3]) + '\n'
        return output
    

def select_other(good, price):
    conn = sqlite3.connect('Adatbazis/expenses.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_OTHER, (good, price))
        list = c.fetchall()
        c.close()
        output = ''
        for x in list:
            output = output + str(x[1]) + ' ' + str(x[2]) + ' ' + str(x[3]) + '\n'
        return output