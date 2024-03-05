# Author: Junfei Ding, Guizhou University, Date: 2023-11-13
import numpy as np
def powerA(A, k=50, tol=1e-6):
    x = np.random.rand(A.shape[1])
    x = x / np.linalg.norm(x)
    lambda_old = 0
    for i in range(k):
        Ax = np.dot(A, x)
        x = Ax / np.linalg.norm(Ax)
        lambda_new = np.dot(x.T, Ax)
        if np.abs(lambda_new - lambda_old) < tol:
            return lambda_new, x
        lambda_old = lambda_new
    print("Didn't converge within the specified number of iterations.")
    return lambda_new, x
if __name__=="__main__":
    A = np.array([
        [6, 2, 1, 3],
        [2, 3, 1, 1],
        [1, 1, 5, 2],
        [3, 1, 2, 7]])
    eigval, eigvec = powerA(A)
    print("Dominant Eigenvalue and Eigenvector calculated by power method: ")
    print(eigval,eigvec)
    print("By numpy: ", )
    npeigvals, npeigvecs = np.linalg.eig(A)
    print(npeigvals[0],npeigvecs[:,0])