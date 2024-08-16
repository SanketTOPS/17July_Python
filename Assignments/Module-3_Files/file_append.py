fl=open('test.txt','a')

id=input("Enter your ID:")
name=input("Enter your Name:")
city=input("Enter your City:")

fl.write(f"ID={id}\nName={name}\nCity={city}\n")