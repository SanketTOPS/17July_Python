import pandas

mydata={
    'tech':['Python','JAVA','PHP','Angular'],
    'frmw':['Django','Spring','Laravel','JS Farmework']
}

dt=pandas.DataFrame(mydata)
print(dt)