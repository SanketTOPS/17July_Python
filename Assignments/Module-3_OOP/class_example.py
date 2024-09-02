class student:
    stid=12
    stnm="Sanket"

    def myfunc(self):
        print("This is student clsas!")
    
    def getsum(self,a,b):
        print("Sum:",a+b)

#Object of class
st=student()
print("ID:",st.stid)
print("Name:",st.stnm)
st.myfunc()
st.getsum(12,56)
