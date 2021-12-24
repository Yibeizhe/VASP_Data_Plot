import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
# Set times New Times Roman
rcParams['font.family']='serif'
rcParams['font.serif']=['Times New Roman']
# Set spines size
rcParams['axes.linewidth'] =1
#This script only used to plot the phonon of the structure
#Usually the data is in phonon.out
# np.genfromtxt can remove the empty line in file.
phonon=np.genfromtxt('PhononBand.dat')
#kpoints and segments are set in band.conf
kpoints=201
segments=3
# k points high symmetry points
ksym_name=[r'$\Gamma$','M','K',r'$\Gamma$']
# The total number of k points in a band
total_kpoints=kpoints*segments
# K points values of each band line.
k_value=phonon[0:total_kpoints,0]

# Return all the high symmetry points values
def ksym(ks=k_value):
    ksym = []
    ksym.append(ks[0])
    for i in range(len(ks)-1):
        if ks[i]==ks[i+1]:
            ksym.append(ks[i])
    ksym.append(ks[-1])
    return ksym

ksym=ksym()
fig = plt.figure(figsize=(4, 3), dpi=300)
n_bands=int(int(phonon.shape[0])/total_kpoints)
for i in range(n_bands):
    plt.plot(k_value,phonon[i*total_kpoints:(i+1)*total_kpoints,1],linewidth=1.5,color='lightseagreen')
plt.xticks(ksym,ksym_name)
for i in ksym:
    plt.axvline(x=i, color='grey', linewidth=0.5, linestyle='--')
plt.ylim(phonon[:,1].min()-1,phonon[:,1].max()+1)
plt.xlim(k_value.min(),k_value.max())
plt.axhline(y=0,linestyle='--',color='red',linewidth=0.5)
plt.tick_params(direction='in')
plt.ylabel('Frequency(THz)')
# plt.spines.set_linewidth(5)
fig.savefig('MnN2_T_phono.png')
plt.show()
