import matplotlib.pyplot as plt
import numpy as np
class Eigenval():
    def __init__(self,eigenval):
        with open(eigenval,'r') as eigen:
            self.eigen=eigen.readlines()

            # The 1st number in 6th line of EIGNVAL file is the number of electrons
            self.electron = self.eigen[5].split()[0]
            print('There are {} electrons'.format(self.electron))

            # The 2nd number in 6th line of EIGNVAL file is the number of bands
            self.ks=int(self.eigen[5].split()[1])
            print('There are {} k points'.format(self.ks))

            # The 3rd number in 6th line of EIGNVAL file is the number of bands
            self.nbands = int(self.eigen[5].split()[2])
            print('There are {} bands'.format(self.nbands))

