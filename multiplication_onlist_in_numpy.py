import numpy as np

l1 = [1, 2, 3, 4, 5]
print(l1)
l2 = [6, 7, 8, 9, 10]
print(l2)
# print(l1*l2)       will get error

l01 = np.array(l1)
l02 = np.array(l2)

print('product of above list: ', l01*l02)
