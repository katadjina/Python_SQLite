import sqlite3

cnx = sqlite3.connect('movies.db')

cursor = cnx.cursor()

#cursor.execute("INSERT INTO Movies VALUES ('Melancholia', 'Lars Von Trier' , 2000) ")
#cursor.execute("SELECT * FROM Movies")

#films = [ ('Toto', 'Lorem Ipsum', 2022),
 #        ('Toto', 'Lorem Ipsum', 2022),
  #       ('Avatar', 'Lorem Ipsum', 2012)
   #      ]

#cursor.executemany('Insert INTO Movies VALUES(?,?,?)' , films)
#
#records = cursor.execute("SELECT * FROM Movies")
#print(cursor.fetchone())
#print(cursor.fetchall())


#for record in records:
 #   print(record)
 
 
 #create a tuple stored in a relaease year variable   
release_year = (, 2022)


cursor.execute("SELECT * FROM Movies WHERE year=?", release_year)    


print(cursor.fetchall())
    
cnx.commit();
cnx.close();