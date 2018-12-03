import psycopg2

def create_table():
    conn=psycopg2.connect("dbname='database 1' user='postgres' password='sreeram123' host='localhost' port='5432'")
    cur=conn.cursor() #need to creaate a cursor method to connection object
    cur.execute("CREATE TABLE IF NOT EXISTS classroom (name TEXT, rollno TEXT,regno INTEGER, CGPA REAL)")#need to enter sql code in quotes here
    conn.commit()
    conn.close()
create_table()
def insert(name,rollno,regno,cgpa):
    conn=psycopg2.connect("dbname='database 1' user='postgres' password='sreeram123' host='localhost' port='5432'")
    cur=conn.cursor() #need to creaate a cursor method to connection object
    cur.execute("INSERT INTO classroom VALUES (%s,%s,%s,%s)",(name,rollno,regno,cgpa))
    conn.commit()
    conn.close()
#insert("Sivaramakrishnan","16CS242",104171,8.0)
#insert("Siva","16CS108",104170,-1.0)
#insert("Sanjay Prashadh","16CS222",104149,-1.0)
def view():
    conn=psycopg2.connect("dbname='database 1' user='postgres' password='sreeram123' host='localhost' port='5432'")
    cur=conn.cursor() #need to creaate a cursor method to connection object
    cur.execute("SELECT * FROM classroom")#no commit method bcz no need to update anything in the table
    rows=cur.fetchall()
    conn.close()
    return rows
def delete(rollno):
    conn=psycopg2.connect("dbname='database 1' user='postgres' password='sreeram123' host='localhost' port='5432'")
    cur=conn.cursor() #need to creaate a cursor method to connection object
    cur.execute("DELETE FROM classroom WHERE rollno=%s",(rollno,))#need to add , in end bcuz of psycopg2 (required)
    conn.commit()
    conn.close()
#print(view())
#delete("16CS242")
print(view())
def update(cgpa,rollno):
    conn=psycopg2.connect("dbname='database 1' user='postgres' password='sreeram123' host='localhost' port='5432'")
    cur=conn.cursor() #need to creaate a cursor method to connection object
    cur.execute("UPDATE classroom SET cgpa=%s WHERE rollno=%s ",(cgpa,rollno))#no need a last "," if more than one data
    conn.commit()
    conn.close()
#print(view())
#update(-1.0,"16CS222")
#print(view())
