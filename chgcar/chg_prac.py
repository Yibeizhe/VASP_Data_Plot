import numpy as np
# import matplotlib.pyplot as plt
import time
class Chgcar():
    def __init__(self,chg):
        with open(chg,'r') as ch:
            self.chgcar=ch.readlines()
        #get the elements
        self.elements_name=self.chgcar[5].split()
        #get the corresponding atoms number of each elements
        self.elements_cor_num=self.chgcar[6].split()
        self.atoms_num=sum(np.array(self.elements_cor_num,dtype='int'))
        #find the NG(X,Y,Z)F
        self.fft_line=self.atoms_num+9
        print(self.fft_line)
        self.fft=np.array(self.chgcar[self.fft_line].split(),dtype=int)
        print("FFT Grid: {}".format(self.fft))
        if np.prod(self.fft) % 5 == 0:
            self.charge_lines=int(np.prod(self.fft)/5)
        else:
            self.charge_lines=int(np.prod(self.fft)//5+1)
        print("The charge density is writed as {} lines in CHGCAR".format(self.charge_lines))
        # get the scale rate from the second line
        self.scale_rate = float("".join(self.chgcar[1].split()))
        # get a,b,c axis of the lattice,respectively.
        self.axis_a = np.array(self.chgcar[2].split(), dtype=float)
        self.axis_b = np.array(self.chgcar[3].split(), dtype=float)
        self.axis_c = np.array(self.chgcar[4].split(), dtype=float)

    def chg_total(self):
        chg_density=np.array(self.chgcar[self.fft_line + 1:self.fft_line+self.charge_lines+1])
        print(chg_density.shape)
        print(chg_density)
        return chg_density
if __name__=="__main__":
    chg=Chgcar('CHGCAR12')
    chg.chg_total()