import numpy as np
matrix = np.arange(1,26).reshape(5,5)
print(matrix)
print(matrix[2:,1:])
print(matrix[:3,1])
row_sums = np.sum(matrix, axis=1).reshape(5,1)
print(row_sums)
col_sums = np.sum(matrix, axis=0).reshape(1,5)
print(col_sums)
