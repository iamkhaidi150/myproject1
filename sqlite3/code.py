> SQlite3 can be integrated with Python using sqlite3 module which was written by Gerhard Haring.
 
> Use sqlite3 module and it is shipped free from python 2.5.x
 
> To use sqlite3 module you must first create a connection object that represents the database and optionally
  you can create cursor object which will help you in executing all the SQL statements.
 
 
c111tqc-vm19:~ # cat sqlite.py
#!/usr/bin/python
import sqlite3
conn=sqlite3.connect("test.db")
print "Opened Database succesfully"
conn.execute('''CREATE TABLE COMPANY
        (ID INT PRIMARY KEY NOT NULL,
         NAME TEXT NOT NULL,
         AGE  INT  NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')
print "Table created succesfully"
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES(1, 'Paul', 32, 'california',20000.00)");
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES(2, 'Allen', 25, 'Texas', 15000.00)");
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES(3, 'Teddy', 36, 'Norway', 25000.00)");
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES(4, 'Ed', 28, 'Richmond', 32000.00)");
conn.commit()
print "Records Created Succesfully"
 
conn.close()
c111tqc-vm19:~ # cat sqlite_1.py
#!/usr/bin/python
import sqlite3
conn=sqlite3.connect("test.db")
print "Opened Database succesfully"
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES(1, 'Paul', 32, 'california',20000.00)");
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES(2, 'Allen', 25, 'Texas', 15000.00)");
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES(3, 'Teddy', 36, 'Norway', 25000.00)");
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES(4, 'Ed', 28, 'Richmond', 32000.00)");
conn.commit()
print "Records Created Succesfully"
 
conn.close()
c111tqc-vm19:~ # cat sqlite_2.py
#!/usr/bin/python
import sqlite3
conn=sqlite3.connect("test.db")
print "Opened Database succesfully"
cursor=conn.execute("SELECT ID,NAME,AGE,ADDRESS,SALARY from COMPANY")
print "ID       NAME    AGE     ADDRESS SALARY"
for row in cursor:
        print "%d\t%s\t%d\t%s\t%.2f"    %(row[0],str(row[1]),row[2],str(row[3]),float(row[4]))
print "Operation done succesfully"
conn.close()
c111tqc-vm19:~ # cat sqlite_3.py
#!/usr/bin/python
import sqlite3
conn=sqlite3.connect("test.db")
print "Opened Database succesfully"
conn.execute("UPDATE COMPANY set SALARY=25000.00 where ID=1")
conn.commit
print "Total number of rows updated", conn.total_changes
print "checking the db after the change"
cursor=conn.execute("SELECT ID,NAME,AGE,ADDRESS,SALARY from COMPANY")
print "ID       NAME    AGE     ADDRESS SALARY"
for row in cursor:
        print "%d\t%s\t%d\t%s\t%.2f"    %(row[0],str(row[1]),row[2],str(row[3]),float(row[4]))
conn.close()
 
c111tqc-vm19:~ #
 
 
#!/usr/bin/python
import sqlite3
conn=sqlite3.connect("test.db")
print "Opened Database succesfully"
conn.execute("DELETE from  COMPANY where ID=1")
conn.commit
print "Total number of rows updated", conn.total_changes
print "checking the db after the change"
cursor=conn.execute("SELECT ID,NAME,AGE,ADDRESS,SALARY from COMPANY")
print "ID       NAME    AGE     ADDRESS SALARY"
for row in cursor:
        print "%d\t%s\t%d\t%s\t%.2f"    %(row[0],str(row[1]),row[2],str(row[3]),float(row[4]))
conn.close()
 
c111tqc-vm19:~ #
