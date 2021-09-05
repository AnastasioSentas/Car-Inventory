import psycopg2


def Table_create():
    
    connector=psycopg2.connect("dbname = 'Cars' user = 'postgres' password = '123456789' host='localhost' port ='5432'" )

    cur= connector.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS BMW (cartype TEXT,price REAL,VIN TEXT)')
    
    connector.commit()

    connector.close()


def Inserter(car,price,VIN):

    connector=psycopg2.connect("dbname = 'Cars' user = 'postgres' password = '123456789' host='localhost' port ='5432'")

    cur= connector.cursor()

    cur.execute('INSERT INTO BMW VALUES (%s,%s,%s)' ,(car,price,VIN))
    
    connector.commit()

    connector.close()


Table_create()
#Inserter('BMW X1 Sdrive 16d',37600,'3N24567')

def View():
    connector=psycopg2.connect("dbname = 'Cars' user = 'postgres' password = '123456789' host='localhost' port ='5432'")

    cur= connector.cursor()

    cur.execute('SELECT * FROM BMW')

    DATA = cur.fetchall()

    connector.close()
    

    return DATA

   
def delete(cartype):
    connector=psycopg2.connect("dbname = 'Cars' user = 'postgres' password = '123456789' host='localhost' port ='5432'")

    cur= connector.cursor()

    cur.execute('DELETE FROM BMW WHERE cartype=%s',(cartype,))

    connector.commit()

    connector.close()
    
def update(cartype,price,vin):

    connector=psycopg2.connect("dbname = 'Cars' user = 'postgres' password = '123456789' host='localhost' port ='5432'")

    cur= connector.cursor()

    cur.execute('UPDATE BMW SET cartype =%s, price=%s WHERE VIN=%s',(cartype,price,vin))

    connector.commit()
    
    connector.close()



akis =delete('BMW X1 Sdrive 16d') * 3

Inserter('BMW X1 Sdrive 16d',37600,'3N24567')
update('BMW X2 Xdrive 18i',1,'3N24567')   
print(View())