import time 
import mysql.connector
try:
    sql="create database LPU"
    con=mysql.connector.connect(host="localhost",user="root",password="")
    cursor=con.cursor()
    cursor.execute(sql)
    print('DataBase is created sucessfully ...')
except mysql.connector.DatabaseError as e:
    if con: 
        con.rollback()
        print("Exception name is:",e)
finally:
    if cursor:
        cursor.close()
    elif con:
        con.close()
print()
time.sleep(2)
print("End of an application")
