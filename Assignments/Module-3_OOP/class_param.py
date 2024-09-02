class studinfo:
    def printdata(self,stid,stnm):
        print("ID:",stid)
        print("Name:",stnm)


st=studinfo()
#st.printdata(101,'Sanket') #static
x=input("Enter an ID:")
y=input("Enter a Name:")
st.printdata(x,y)
