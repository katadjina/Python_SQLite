import sqlite3


cnx = sqlite3.connect('movies.db')

cursor = cnx.cursor();

cursor.execute(''' CREATE TABLE IF NOT EXISTS Movies (Title TEXT, Director TEXT, Year INT)''')
#no datetime type in SQLite

cnx.commit();
cnx.close();