# Author: Junfei Ding, Guizhou University, Date: 2023-11-06
import numpy as np
def gram_schmidt(A):
    """
    Applies the Gram-Schmidt method to matrix A to
    orthogonalize its rows.
    Parameters:
    - A (numpy.ndarray): The matrix to be orthogonalized.
    Returns:
    - Q (numpy.ndarray): The orthogonalized matrix.
    """
    m, n = A.shape
    Q = np.zeros((m, n))
    for j in range(n):
        # Start with the j-th column of A
        v = A[:, j]
        for i in range(j):
            # Subtract the projection of A[:, j]
            # onto the i-th column of Q
            v = v - np.dot(Q[:, i], A[:, j]) * Q[:, i]
        # Normalize the resulting vector
        Q[:, j] = v / np.linalg.norm(v)
    return Q

def is_orthogonal(Q):
    """
    Check if the columns of matrix Q are orthogonal and normalized.
    Args:
    - Q (numpy.ndarray): The matrix to be verified.
    Returns:
    - bool: True if the columns of Q are orthogonal and normalized, False otherwise.
    """
    m, n = Q.shape
    for i in range(n):
        for j in range(n):
            dot_product = np.dot(Q[:, i], Q[:, j])
            if i != j and not np.isclose(dot_product, 0):
                # Columns are not orthogonal
                return False
            elif i == j and not np.isclose(dot_product, 1):
                # Columns are not normalized
                return False
    return True

if __name__=="__main__":
    A = np.array([[6, 2, 1],
                  [2, 3, 1],
                  [1, 1, 1]])
    # Orthogonalize the matrix A
    Q = gram_schmidt(A)
    print("Orthogonalized Matrix Q:\n", Q)

    # Verify if the matrix Q is orthogonal
    print("Is Q orthogonal?", is_orthogonal(Q))