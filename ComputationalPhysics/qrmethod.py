# Author: Junfei Ding, Guizhou University, Date: 2023-11-06

import numpy as np
from QR_Decompose import QR

def qrmet(inA,kmax=100):
    A = np.copy(inA)
    for k in range(1,kmax):
        Q, R = QR(A)
        A = R@Q
        print(k, np.diag(A))

    qreigvals = np.diag(A)
    return qreigvals

if __name__ == '__main__':
    A = np.array([[6, 2, 1],
                  [2, 3, 1],
                  [1, 1, 1]])
    qreigvals = qrmet(A,6)
    print(" ")
    npeigvals, npeigvecs = np.linalg.eig(A); print(npeigvals)
