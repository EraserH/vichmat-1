import numpy as np

first_matrix = np.random.randint(0, 11, (3, 2))
second_matrix = np.random.randint(0, 11, (2, 3))
result_matrix = np.dot(first_matrix, second_matrix)

print("Первая матрица:")
print(first_matrix)
print("Вторая матрица:")
print(second_matrix)
print("\nРезультат умножения первой матрицы на вторую:")
print(result_matrix)