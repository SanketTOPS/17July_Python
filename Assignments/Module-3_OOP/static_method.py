class student:
    @staticmethod
    def getdata():
        print("This is getdata!")
    
    @staticmethod
    def getsum(a,b):
        print("Sum:",a+b)


st=student()
st.getdata()
st.getsum(12,56)