import sqlite3


def connector():
    
    connector=sqlite3.connect('Cars.db' )

    cur= connector.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS BMW (id INTEGER PRIMARY KEY, cartype TEXT,year INTEGER ,price REAL,VIN TEXT)')
    
    connector.commit()

    connector.close()


def insert(car,year,price,vin):

    connector=sqlite3.connect('Cars.db' )

    cur= connector.cursor()

    cur.execute("INSERT INTO BMW VALUES(NULL,?,?,?,?)",(car,year,price,vin))

    connector.commit()

    connector.close()

def view():

    connector=sqlite3.connect('Cars.db' )

    cur= connector.cursor()

    cur.execute('SELECT * FROM BMW')

    DATA=cur.fetchall() 

    connector.commit()

    connector.close()

    return DATA

def update(id,car,year,price,vin):
    connector=sqlite3.connect('Cars.db' )

    cur= connector.cursor()

    cur.execute('UPDATE BMW SET cartype=?,year=?,price=?,VIN=? WHERE id=?',(car,year,price,vin,id))

    connector.commit()

    connector.close()

    

def delete(id):

    connector=sqlite3.connect('Cars.db' )

    cur= connector.cursor()

    cur.execute('DELETE  FROM BMW WHERE id=?' ,(id,))

    cur.execute("DELETE FROM BMW WHERE cartype='BMW X2 Xdrive 18i'")

    connector.commit()

    connector.close()

def search(car='',year='',price='',vin=''):
    
    connector=sqlite3.connect('Cars.db' )

    cur= connector.cursor()

    cur.execute("SELECT * FROM BMW WHERE cartype=? OR year=? OR price=? OR VIN=?" ,(car,year,price,vin))

    results=cur.fetchall()

    connector.commit()

    connector.close()

    return results

    


connector()

#insert('BMW X5 Xdrive 18i', 2021, 37500.0, '3N21768')
#delete(5)
#update(1,'akys',1,2,'akis')
#print(view())