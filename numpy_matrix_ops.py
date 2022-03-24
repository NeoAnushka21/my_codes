import numpy as np

A = np.array([[2, 1, 3],
              [4, 9, 10],
              [7, -3, 9]])
print(A)
print('Rank: ', np.linalg.matrix_rank(A))
print('trace:', np.trace(A))
print('Determinant:', np.linalg.det(A))

print('Power :', np.linalg.matrix_power(A, 3))
print('inverse:', np.linalg.inv(A))