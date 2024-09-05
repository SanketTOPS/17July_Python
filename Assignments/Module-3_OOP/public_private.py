class studinfo:
    __stid=12 #private
    __stnm="Sanket" #private

    def getdata(self):
        print("This is getdata!")
    
    def __printdata(self):
        print("ID:",self.__stid)
        print("Name:",self.__stnm)
    
    def result(self):
        self.__printdata()

st=studinfo()
#print("ID:",st.stid)
#print("Name:",st.stnm)
st.getdata()
#st.printdata()
st.result()