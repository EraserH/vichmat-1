import numpy as np

matrix = np.random.randint(0, 11, (7, 7))
print("Матрица:")
print(matrix)
matrix.transpose()
print("\nТранспонированная матрица:")
print(matrix)

determinant = np.linalg.det(matrix)
print(determinant)
