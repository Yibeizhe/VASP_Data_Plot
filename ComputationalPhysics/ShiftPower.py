import numpy as np
from gaussianpivot import gaussian_pivot
def ShiftPower(A, sigma, tol=1e-8, max_iter=1000):
    """
    Parameters
    ----------
    A : ndarray, shape (n,n)
        Input matrix
    x0 : ndarray, shape (n,)
        Initial guess for the eigenvector
    sigma : float
        The shift value
    tol : float, optional
        Convergence tolerance
    max_iter : int, optional
        Maximum number of iterations

    Returns
    -------
    lambda_min : float
        Eigenvalue closest to sigma
    v : ndarray, shape (n,)
        Corresponding eigenvector
    """
    x0 = np.random.rand(A.shape[0])
    x = x0 / np.linalg.norm(x0)
    I = np.eye(A.shape[0])
    B = A - sigma * I  # Shifted matrix

    for i in range(max_iter):
        # y = np.linalg.solve(B, x)
        y=gaussian_pivot(B, x)
        x = y / np.linalg.norm(y)
        # Rayleigh quotient to approximate the eigenvalue
        lambda_min = np.dot(x.T, np.dot(A, x)) / np.dot(x.T, x)
        # Check for convergence
        if np.linalg.norm(np.dot(B, x) - (lambda_min - sigma) * x) < tol:
            break
    else:
        raise ValueError(f"Failed to converge within {max_iter} iterations")

    return lambda_min, x

if __name__=="__main__":
    # Usage
    A = np.array([[6, 2, 1], [2, 3, 1], [1, 1, 1]])
    # A = np.array([
    #     [6, 2, 1, 3],
    #     [2, 3, 1, 1],
    #     [1, 1, 5, 2],
    #     [3, 1, 2, 7]])
    sigma = 9  # Chosen shift value
    eigenvalue, eigenvector = ShiftPower(A, sigma)
    npeigenval,npeigenvec=np.linalg.eig(A)
    print(npeigenval,npeigenvec)

    print('Eigenvalue:', eigenvalue)
    print('Eigenvector:', eigenvector)