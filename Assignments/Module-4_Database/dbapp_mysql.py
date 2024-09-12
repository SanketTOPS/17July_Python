import pymysql

try:
    dbcon=pymysql.connect(host='localhost',user='root',password='',database='newdata')
    print("Database Connected!")
except Exception as e:
    print(e)

cr=dbcon.cursor()

#Table Create
tbl_create="create table studinfo(id integer primary key auto_increment,name varchar(20),city varchar(20))"
try:
    cr.execute(tbl_create)
    print("Table created!")
except Exception as e:
    print(e)

#Insert data
"""insert_data="insert into studinfo(name,city)values('sanket','rajkot'),('nirav','baroda'),('ashok','surat'),('hitesh','navsari')"
try:
    cr.execute(insert_data)
    dbcon.commit()
    print("Record inserted!")
except Exception as e:
    print(e)"""

#Update Data
update_data="update studinfo set name='prasiddh',city='ahmedabad' where id=4"
try:
    cr.execute(update_data)
    dbcon.commit()
    print("Record Updated!")
except Exception as e:
    print(e)

#Delete Data
delete_data="delete from studinfo where id=4"
try:
    cr.execute(delete_data)
    dbcon.commit()
    print("Record Deleted!")
except Exception as e:
    print(e)


#Show Data

show_data="select * from studinfo"
try:
    cr.execute(show_data)
    #data=cr.fetchall()
    #data=cr.fetchmany(2)
    data=cr.fetchone()
    print(data)
except Exception as e:
    print(e)