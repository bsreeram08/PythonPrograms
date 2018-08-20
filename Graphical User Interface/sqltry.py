import sqlite3

def create_table():
    connection=sqlite3.connect("databasetry.db")
    cur=connection.cursor()
    cur.execute("CREATE TABLE SUBJECTS(MATHS INTEGER,COMPUTER INTEGER,PHYSICS INTEGER, ENGLISH INTEGER,CHEMISTRY INTEGER)")
    connection.commit()
    connection.close()
def insert_table(maths,computer,physics,english,chemistry):
    connection=sqlite3.connect("databasetry.db")
    cur=connection.cursor()
    cur.execute("INSERT INTO SUBJECTS VALUES(?,?,?,?,?)",(maths,computer,physics,english,chemistry))
    connection.commit()
    connection.close()
def display():
    connection=sqlite3.connect("databasetry.db")
    cur=connection.cursor()
    cur.execute("SELECT * FROM SUBJECTS")
    rows=cur.fetchall()
    connection.close()
    return(rows)
def delete(maths):
    connection=sqlite3.connect("databasetry.db")
    cur=connection.cursor()
    cur.execute("DELETE FROM SUBJECTS WHERE MATHS=?",(maths,))
    connection.commit()
    connection.close()
def update(maths,computer,physics,english,chemistry,maths1):
    connection=sqlite3.connect("databasetry.db")
    cur=connection.cursor()
    cur.execute("UPDATE SUBJECTS SET MATHS=?,COMPUTER=?,PHYSICS=?,ENGLISH=?,CHEMISTRY=? WHERE MATHS=?",(maths,computer,physics,english,chemistry,maths1))
    connection.commit()
    connection.close()
insert_table(89,74,45,98,86)
delete(88)
update(98,57,77,87,67,98)
print(display())
