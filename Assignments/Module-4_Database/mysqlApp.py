import pymysql

try:
    dbcon=pymysql.connect(host='localhost',user='root',password='',database='newwdb')
    print("Database connected!")
except Exception as e:
    print(e)

cr=dbcon.cursor()

#Table Create
create_tbl="create table studinfo(id integer primary key auto_increment,name text,city text)"
try:
    cr.execute(create_tbl)
    print("Table created!")
except Exception as e:
    print(e)


#Insert Data
insert_data="insert into studinfo(name,city)values('sanket','rajkot'),('nirav','baroda'),('pankaj','surat'),('ashok','morbi'),('hitesh','jamnagar')"
try:
    cr.execute(insert_data)
    dbcon.commit()
    print("Record Inserted!")
except Exception as e:
    print(e)
