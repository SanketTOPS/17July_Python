fl=open('new.txt','w')

id=input("Enter your ID:")
name=input("Enter your Name:")
city=input("Enter your City:")

"""fl.write(id)
fl.write(name)
fl.write(city)"""

fl.write(f"ID={id}\nName={name}\nCity={city}")