import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    row = len(A)
    col = len(A[0])

    arr = [[0] * row for _ in range(col)]

    for i in range(row):
        for j in range(col):
            arr[j][i] = A[i][j]

    return np.array(arr)