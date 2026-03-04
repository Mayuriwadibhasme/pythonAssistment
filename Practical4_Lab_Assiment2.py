import numpy as np

# Function to take matrix input from user
def input_matrix(rows, cols, name):
    print(f"Enter elements for {name} ({rows}x{cols}):")
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            val = int(input(f"Enter element [{i+1},{j+1}]: "))
            row.append(val)
        matrix.append(row)
    return np.array(matrix)

# Input matrices
matrix1 = input_matrix(5, 3, "Matrix A")
matrix2 = input_matrix(3, 2, "Matrix B")

# Multiply matrices
product_matrix = np.dot(matrix1, matrix2)

# Print results
print("\nMatrix A (5x3):")
print(matrix1)

print("\nMatrix B (3x2):")
print(matrix2)

print("\nProduct Matrix (5x2):")
print(product_matrix)
