import time 
import mysql.connector
try:
    sql="alter table Produts rename P5"
    con=mysql.connector.connect(host="localhost",user="root",password="",database='lpu')
    cursor=con.cursor()
    cursor.execute(sql)
    print('Table is renamed successfully ...')
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
