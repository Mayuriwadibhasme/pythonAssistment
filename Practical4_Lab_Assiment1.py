import numpy as np

# Part (a): Generate a 4x4 identity matrix
identity_matrix = np.identity(4)
print("4x4 Identity Matrix:")
print(identity_matrix)

# Part (b): Generate two 3x3 random integer matrices (values between 1 and 9)
matrix1 = np.random.randint(1, 10, (3, 3))
matrix2 = np.random.randint(1, 10, (3, 3))

print("\nMatrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

# Matrix Addition
addition_result = matrix1 + matrix2
print("\nMatrix Addition Result:")
print(addition_result)

# Matrix Multiplication
multiplication_result = np.dot(matrix1, matrix2)
print("\nMatrix Multiplication Result:")
print(multiplication_result)
