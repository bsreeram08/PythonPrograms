import sqlite3

def create_table():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor() #need to creaate a cursor method to connection object
    cur.execute("CREATE TABLE IF NOT EXISTS classroom (name TEXT, rollno TEXT,regno INTEGER, CGPA REAL)")#need to enter sql code in quotes here
    conn.commit()
    conn.close()
def insert(name,rollno,regno,cgpa):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor() #need to creaate a cursor method to connection object
    cur.execute("INSERT INTO classroom VALUES (?,?,?,?)",(name,rollno,regno,cgpa))
    conn.commit()
    conn.close()
#insert("Sivaramakrishnan","16CS242",312316104170,8.0)
#insert("Sanjay Prashadh","16CS222",312316104149,-1.0)
def view():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor() #need to creaate a cursor method to connection object
    cur.execute("SELECT * FROM classroom")#no commit method bcz no need to update anything in the table
    rows=cur.fetchall()
    conn.close()
    return rows
def delete(rollno):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor() #need to creaate a cursor method to connection object
    cur.execute("DELETE FROM classroom WHERE rollno=?",(rollno,))#need to add , in end bcuz of sqlite3 (required)
    conn.commit()
    conn.close()
#print(view())
#delete("16CS222")
#print(view())
def update(cgpa,rollno):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor() #need to creaate a cursor method to connection object
    cur.execute("UPDATE classroom SET cgpa=? WHERE rollno=? ",(cgpa,rollno))#no need a last "," if more than one data
    conn.commit()
    conn.close()
print(view())
#update(7.1,"16CS222")
#print(view())
