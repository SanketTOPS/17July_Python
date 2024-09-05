class master:
    def getdata(self,id,name): #original
        print("ID:",id)
        print("Name:",name)

class home(master):
    def getdata(self, id, name): #xerox
        return super().getdata(id, name)
    
class about(master):
    def getdata(self, id, name):
        return super().getdata(id, name)


h=home()
a=about()
h.getdata(101,'Sanket')
a.getdata(102,'Ashok')