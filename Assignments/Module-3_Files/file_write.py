fl=open('temp.txt','w')

fl.write("Good Afternoon Students!")

if fl.writable():
    print("Yes..")
else:
    print("Noo")


