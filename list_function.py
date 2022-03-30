L1 = ['cat', 1, 'dog', 2, 'rabbit', 3, 'horse', 4, 'tiger', 5, 'lion', 6]


index = L1.index(3)
print(index)

L1.append('cow')
print(L1)

L2 = ['hen', 8]
L1.extend(L2)
print(L1)

L1.insert(13,7)
print(L1)

print(L1.count(1))