import time 
import mysql.connector
try:
    sql="drop database LPU"
    con=mysql.connector.connect(host="localhost",user="root",password="",database='LPU')
    cursor=con.cursor()
    cursor.execute(sql)
    con.commit()
    print('Database is deleted successfully ...')
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
