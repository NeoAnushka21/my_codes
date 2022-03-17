str01 = 'My name is Anushka'
print(str01)
print(str01.lower())
print(str01.upper())
print(str01.find('A'))
print(str01.find('shk'))
print(str01.replace('Anu', ' '))

list1 = ['anuskakahka','anustatahka']
list2 = []
start = 4
end = 8
for i in list1:
    if len(i) > end:
        i = i[0: start:] + i[end + 1::]
        list2.append(i)
print(list2)



