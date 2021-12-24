import numpy as np
import matplotlib.pyplot as plt
plt.rc('font',family='Times New Roman')
poten_file='GBs1-Br_Potenetial.dat'
files=['tetra-MnN2_MoN2_potential.dat','tetra-MnN2_WN2_potential.dat']
efermi={'MnN2_MoN2':-4.1297,'MnN2_WN2':-4.06404814}

potential=np.loadtxt(files[1],comments='#')
fig = plt.figure(figsize=(4,3), dpi=300)
color1='#39A1FF'
color2='#FF7F50'
plt.plot(potential[:,0],potential[:,1],color=color1,lw=2)
plt.xlim(5,20)
# plot fermi level

fermi_level=efermi['MnN2_WN2']
plt.axhline(y=fermi_level, linestyle='--', color='red', linewidth=1.5)
plt.tick_params(axis='both',direction='in',labelsize=8)
plt.xlabel("Position along z-axis(Å)")
plt.ylabel('Effective potential (eV)')
plt.savefig(files[0]+'.png',bbox_inches='tight')
plt.show()