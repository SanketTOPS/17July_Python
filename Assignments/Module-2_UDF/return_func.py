def getdata(id,name):
    return id,name

"""x=getdata(101,"Sanket")
print(x[1])"""
    
def printdata():
    x=getdata(101,"Sanket")
    print("ID:",x[0])
    print("Name:",x[1])


printdata()