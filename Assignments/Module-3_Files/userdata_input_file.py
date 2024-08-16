fl=open('stdata.txt','a')

n=int(input("Enter number of students:"))

for i in range(n):
    id=input("Enter your ID:")
    nm=input("Enter your Name:")
    ct=input("Enter your City:")

    fl.write(f"ID:{id}\nName:{nm}\nCity:{ct}\n")