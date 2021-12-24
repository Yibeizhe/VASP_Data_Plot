import  numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family']='serif'
rcParams['font.serif']=['Times New Roman']
mag_Cv=np.loadtxt('E.dat',skiprows=2)
temp=mag_Cv[:,0]
Cv=mag_Cv[:,2]
mag=mag_Cv[:,-1]

# Tc temperature
Tc_pos=Cv.argmax()
Tc=temp[Cv.argmax()]
print('The Tc temperature is {}.'.format(Tc))
c1="blue"
fig, ax1 = plt.subplots()
ax1.set_xlabel('Temperature(K)',fontsize=20)
ax1.set_ylabel('Magnetization$(\mu_B)$',color=c1,fontsize=20)
ax1.tick_params(axis='y',colors=c1,direction='in',labelsize=15)
ax1.tick_params(axis='x',colors='black',direction='in',labelsize=15)
#ax1.spines['left'].set_color(c1)
ax1.plot(temp,mag,'-o',color=c1)

c2='red'
ax2=ax1.twinx()
ax2.plot(temp,Cv,'-o',color=c2)
ax2.spines['right'].set_color(c2)
ax2.spines['left'].set_color(c1)
ax2.tick_params(axis='y',colors=c2)
ax2.set_ylabel(r'$C_v$(a.u.)',color=c2,fontsize=20)

plt.xlim(temp.min(),temp.max())
plt.axvline(x=Tc, color='black', linewidth=1, linestyle='--')
plt.tick_params(direction='in',labelsize=15)

fig.savefig('E_Cv.png',figsize=(3,4),dpi=300,bbox_inches='tight')
fig.show()

