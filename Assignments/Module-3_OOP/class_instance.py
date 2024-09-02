class student:
    stid=12
    stnm="Sanket"

    def getdata(self):
        print("ID:",self.stid)
        print("Name:",self.stnm)

#Object
"""st=student()
st.getdata()
st.stid=40
st.stnm="Ashok"
st.getdata()"""

#Instance
student().getdata()
student().stid=50
student().stnm="Hitesh"
student().getdata()