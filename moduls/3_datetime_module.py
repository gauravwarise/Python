import datetime
dt=datetime.datetime(2022,7,15,15,20,55)
print(dt)
print("MInimum Year: ",datetime.MINYEAR)
print("maximum Year: ",datetime.MINYEAR)
print("UTc is: ",datetime.timezone.utc)
# cdt=datetime.datetime.now()
cdt=datetime.datetime.today()
print(cdt)
print(cdt.year)
print(cdt.month)
print(cdt.day)
print(cdt.hour)
print(cdt.minute)
print(cdt.second)
print(cdt.microsecond)