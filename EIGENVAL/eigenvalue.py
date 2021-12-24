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

    def kpoints(self):
        kpoints = []
        for i in range(self.ks):
            k_coor=[float(i) for i in self.eigen[7+i*(self.nbands+2)].split()[0:3]]
            kpoints.append(k_coor)
        return kpoints

    def high_kpoints(self):
        for i in range(self.ks-1):
            if self.eigen[7+i*(self.nbands+2)].split() == self.eigen[7+(i+1)*(self.nbands+2)].split():
                print(self.eigen[7 + i * (self.nbands + 2)].split())
                print(i)


    def bands(self):
        bands = []
        for band in range(self.nbands):
            band_n_up = []
            for i in range(self.ks):
                band_up=float(self.eigen[8+i*(self.nbands+2)+band].split()[1])
                band_n_up.append(band_up)
            bands.append(band_n_up)
        return bands

t=Eigenval('EIGENVAL')
t.high_kpoints()
print(len(t.bands()[2]))
print(t.kpoints())
plt.plot(t.kpoints(),t.bands()[2])
plt.show()