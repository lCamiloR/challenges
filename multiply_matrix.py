import numpy as np

def multiply_matrices(matrix1, matrix2):
    # Convert lists to numpy arrays
    matrix1 = np.array(matrix1)
    matrix2 = np.array(matrix2)

    # Check if the matrices can be multiplied
    if matrix1.shape[1] != matrix2.shape[0]:
        return "Error: The number of columns in the first matrix must be equal to the number of rows in the second matrix."

    # Multiply the matrices
    result = np.dot(matrix1, matrix2)

    return result.tolist()

matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8], [9, 10], [11, 12]]
print(multiply_matrices(matrix1, matrix2))
