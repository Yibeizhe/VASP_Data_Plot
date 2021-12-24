import numpy as np
import matplotlib.pyplot as plt
class Doscar():
    def __init__(self,dos):
        with open(dos, 'r') as doscar:
            self.doscar=doscar.readlines()

    #The 4th number in the 6th line of the DOSCAR file is fermi level
    def fermi(self):
        self.fer=float(self.doscar[5].split()[3])
        return self.fer

    # The 3th number in the 6th line of the DOSCAR file is the NEDOS
    def nedos(self):
        self.nedos=int(self.doscar[5].split()[2])
        return self.nedos

    #Get the total dos
    def tdos(self):
        import numpy as np
        with open('TDOS.dat', 'w') as t_dos:
            for i in range(6,6+self.nedos()):
                t_dos.write(self.doscar[i])
        self.tdos_array=np.loadtxt('TDOS.dat',dtype='float')
        np.savetxt('DDOS.dat',self.tdos_array[:,0:3])
        return self.tdos_array[:,0:3]


CrBr=Doscar('DOSCAR')
t_dos=CrBr.tdos()
fermi_energy=CrBr.fermi()
energy=t_dos[:,0]-fermi_energy
plt.plot(energy,t_dos[:,1],label='spin-up')
plt.plot(energy,0-t_dos[:,2],label='spin-down')
plt.axvline(x=0,color='r',linestyle='--')
plt.legend()
plt.xlim(-5,5)
plt.title('VS2')
plt.savefig('VS2.png',dpi=300,size=(4,3))
plt.show()