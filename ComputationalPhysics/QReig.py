# Author: Alex Gezerlis
# Numerical Methods in Physics with Python (CUP, 2020)

from ShiftPower import ShiftPower
from QR_Decompose import QR
from qrmethod import qrmet
import numpy as np


def eig(A, eps=1.e-12):
    n = A.shape[0]
    eigvals = np.zeros(n)
    eigvecs = np.zeros((n, n))
    qreigvals = qrmet(A)
    for i, qre in enumerate(qreigvals):
        eigvals[i], eigvecs[:, i] = ShiftPower(A, qre + eps)
    return eigvals, eigvecs



if __name__ == '__main__':
    A = np.array([[6, 2, 1], [2, 3, 1], [1, 1, 1]])
    eigvals,eigvecs=eig(A)
    print(eigvals)
    print(eigvecs)
