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

