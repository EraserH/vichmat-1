import numpy as np

A = np.array([[3, 2, 1], [3, 3, 2], [5, 5, 3]], int)
B = np.array([5, 7, 11])

result = np.linalg.inv(A).dot(B)
result = [round(i) for i in result]

print(result)