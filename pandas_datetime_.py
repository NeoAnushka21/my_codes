from datetime import  date,time

d1 = date.today()
print("Today's date:", d1)

print(d1.day)
print(d1.year)
print(d1.month)

t1 = time(16, 4, 50, 23)
print(t1.hour)
print(t1.minute)
print(t1.second)
print(t1.microsecond)