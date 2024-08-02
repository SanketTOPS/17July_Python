stdata={"id":101,
        "name":"Sanket",
        "sub":"Python"}

"""print(stdata)
print(stdata["name"])
print(stdata.get("id"))

print(len(stdata))
print(stdata.keys())
print(stdata.values())
"""

# ----------------------------------------- #
print(stdata)

"""for i in stdata:
    print(i)"""


"""for i in stdata.values():
    print(i)"""

"""for i in stdata.items():
    print(i)"""

"""for i,j in stdata.items():
    #print(i,j)
    print(f"Key={i} and Value={j}")"""


#stdata['id']=102
#stdata['city']='Rajkot'
#stdata.pop('sub')
#stdata.clear()

del stdata['name']
print(stdata)


#newstdata=stdata.copy()
#print(newstdata)