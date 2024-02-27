dict = {
    "name":"gaurav",
    "city":"kankavli"
}

dict_copy = dict.copy()
dict["pincode"]=871264
print(dict)


d = [
    {
        'id':1,
        'title':'a',
        'complete':False
    },
    {
        'id':2,
        'title':'b',
        'complete':True
    }
    ]
for i in d:
    if i.get('complete')==True:
        print(f"{i.get('title')} task has been completed")
    else:
        pass