import numpy as np

# given equations are
# 3x + 4y =8
# 5x - 9y = 18

# putting coefficients in one array
a = np.array([[3, 4], [5, -9]])
# and constants in other
b = np.array([8, 18])
print('solution is :', np.linalg.solve(a, b))
