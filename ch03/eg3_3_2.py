import numpy as np

"""
这里结合 eg_3_3_3.py 一起看，一维数组是即可以看成是 1 x n 的矩阵，也可以看成是 n x 1 的矩阵
"""
A = np.array([[1, 2], [3, 4], [5, 6]])  # 3 x 2
print(A.shape)
B = np.array([7, 8])  # 2 x 1
print(B.shape)
print(np.dot(A, B))
