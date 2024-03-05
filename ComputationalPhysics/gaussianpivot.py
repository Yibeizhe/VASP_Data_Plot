# Author: Junfei Ding, Guizhou University, Date: 2023-10-9
import numpy as np
def gaussian_pivot(Ai, bi):
    """
    Solve system of linear equations using
    Gaussian Elimination with pivoting.

    Parameters:
    Ai (np.array): Coefficient matrix of size (n, n).
    bi (np.array): Vector of constant terms of size (n, ).

    Returns:
    np.array: Solution vector of size (n, ).
    """
    b = np.copy(bi)
    A = np.copy(Ai)
    n = len(b)
    # Forward elimination
    for i in range(n):
        max_row = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k
        # Swap rows for pivot
        A[i, :], A[max_row, :] = A[max_row, :], A[i, :].copy()
        b[i], b[max_row] = b[max_row], b[i]
        # Zero out below current row
        for k in range(i + 1, n):
            coeff = A[k][i] / A[i][i]
            b[k] -= coeff * b[i]
            A[k, i:] -= coeff * A[i, i:]
    # Backward substitution
    x = np.zeros(n)
    for i in reversed(range(n)):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]
    return x

if __name__ == "__main__":
    A = np.array([[2, 1, -1],
                  [-3, -1, 2],
                  [-2, 1, 2]], dtype=float)
    b = np.array([8, -11, -3], dtype=float)

    x = gaussian_pivot(A, b)
    print("Solution:", x)
    x = np.linalg.solve(A, b)
    print("Numpy: ", x)