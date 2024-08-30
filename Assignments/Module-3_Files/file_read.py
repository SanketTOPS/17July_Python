fl=open('stdata.txt','r')

#print(fl.read())
#print(fl.readline())
#print(fl.readlines())
#print(fl.readlines()[2])

"""for i in fl:
    print(i)"""

if fl.readable():
    print("Yes...")
else:
    print("Noo")