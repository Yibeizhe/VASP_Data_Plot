import numpy as np
import matplotlib.pyplot as plt
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
        chg_den=[]
        for i in range(self.fft_line + 1, self.fft_line+self.charge_lines+1):
            chg_den+=self.chgcar[i].strip('\n').split()
            #print(chg_den)
        chg_density =np.array(chg_den,dtype=float).reshape(self.fft)
        return chg_density

    def lattice_colume(self):
        # Calculate the volume of the lattice which can be obtained from a*(b cross products c)
        volume = self.scale_rate ** 3 \
                 * (self.axis_a[0] * (self.axis_b[1] * self.axis_c[2] - self.axis_b[2] * self.axis_c[1])\
                 - self.axis_a[1] * (self.axis_b[0] * self.axis_c[2] - self.axis_b[2] * self.axis_c[0])\
                 + self.axis_a[2] * (self.axis_b[0] * self.axis_c[1] - self.axis_b[1] * self.axis_c[0]))
        return volume

    def aver_pl_cd(self):
        average_plane_cd=np.zeros(self.fft[2])
        for i in range(self.fft[2]):
            average_plane_cd[i]=np.sum(self.chg_total()[:,:,i])/self.fft[0]/self.fft[1]/self.lattice_colume()
        return average_plane_cd

    def axis_c_num(self):
        axis_length=self.scale_rate*np.sqrt(np.sum(np.power(self.axis_c,2)))
        axis_number=np.linspace(0,axis_length,self.fft[2])
        return axis_number

    def aver_len(self):
        average_plain_density=np.vstack([self.axis_c_num(),self.aver_pl_cd()]).T
        print(average_plain_density)
        return average_plain_density
time_b=time.process_time()
chg=Chgcar('CHGCAR')
np.savetxt('aver_pl_Charge_density.dat',chg.aver_len())
time_e=time.process_time()-time_b
print('total time {} second'.format(time_e))
plt.figure(figsize=(4,3),dpi=300)
plt.plot(chg.axis_c_num(),chg.aver_pl_cd())
plt.title("Average plain charge density")
plt.savefig("Au2.png")
plt.show()
