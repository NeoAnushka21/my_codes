import numpy as np

# numpy basic

my_arr = np.array([[1, 2, 3],
                   [4, 5, 6]])
print('type of array object: ', type(my_arr))
print('dimension: ', my_arr.ndim)
print('shape: ', my_arr.shape)
print('size:', my_arr.size)
print('type of element:', my_arr.dtype)

# creating arrays

my_arr01 = np.array([[1, 2, 3], [4, 5, 6]], dtype='float')              # creating array using list with type float
print(my_arr01)
my_arr02 = np.array(((1, 2, 3), (4, 4, 5)), dtype='complex')            # creating array from tuple
print(my_arr02)
my_arr03 = np.zeros((2, 3))                                             # array with all zeros and given dimension
print(my_arr03)
my_arr04 = np.full((2, 3), 6)                                          # creating array with all 6 and given dimension
print(my_arr04)
my_arr05 = np.random.random((2, 3))                                     # creating array of random numbers
print(my_arr05)
my_arr06 = np.arange(0, 45, 5)                                          # sequence of numbers between 0-45 with step 5
print(my_arr06)
my_arr07 = np.linspace(0, 10, 7)                                        # 7 numbers in range 0 ,10
print(my_arr07)
print('before reshape: ', my_arr)
my_arr00 = my_arr.reshape(3, 2)                                         # change shape from  (2,3) to (3,2)
print('after reshape: ', my_arr00)
my_arr000 = my_arr.flatten()                                            # all elements get into list as sequence
print('after flatting: ', my_arr000)

print('indexing:')
a = np.array([[[1, 2, 3], [4, 5, 6]],
             [[7, 8, 9], [10, 11, 12]]])
print(a[:, :, 2])
print(a[..., 1])

