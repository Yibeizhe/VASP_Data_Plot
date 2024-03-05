# Author: Junfei Ding, Guizhou University, Date: 2023-11-06
import numpy as np
from GramSchmidt import is_orthogonal
def QR(A):
    """
    Perform QR decomposition of matrix A using the Gram-Schmidt process.
    Args:
    - A (numpy.ndarray): The matrix to be decomposed.
    Returns:
    - Q (numpy.ndarray): The orthogonal matrix.
    - R (numpy.ndarray): The upper triangular matrix.
    """
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))

    for j in range(n):
        # Start with the j-th column of A
        v = A[:, j]
        for i in range(j):
            # Compute the dot product
            R[i, j] = np.dot(Q[:, i], A[:, j])
            # Subtract the projection of A[:, j]
            # onto the i-th column of Q from v
            v = v - R[i, j] * Q[:, i]

        # Compute the norm of vector v
        R[j, j] = np.linalg.norm(v)
        # Normalize the vector to get the j-th column of Q
        Q[:, j] = v / R[j, j]
    return Q, R

if __name__=="__main__":

    # Example usage:
    A = np.array([[6, 2, 1],
                  [2, 3, 1],
                  [1, 1, 1]])

    Q, R = QR(A)
    print("Matrix Q (orthogonal):")
    print(Q)
    print("Is Q orthogonal?",is_orthogonal(Q))
    print("Matrix R (upper triangular):")
    print(R)
    print("np.dot(Q,R) is:\n",np.dot(Q,R))
