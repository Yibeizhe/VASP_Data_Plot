import numpy as np
import matplotlib.pyplot as plt
import os
plt.rc('font',family='Times New Roman')
#https://codeantenna.com/a/T1psLDdwRq
def averChar(file):
    averC = np.loadtxt(file, comments='#')
    angst=averC[:,0]
    e=averC[:,1]
    return angst,e

path = os.listdir()
print(path)
ZFOCM=averChar('FeZn2O4_C_MoSe2_pot_aver.dat')
# C=averChar('C_chg_aver.dat')
# MS=averChar('MoSe2_chg_aver.dat')
# ZFO=averChar('FeZn2O4_chg_aver.dat')
ang=ZFOCM[0]
# averC=ZFOCM[1]-C[1]-MS[1]-ZFO[1]
averC=ZFOCM[1]
fig = plt.figure(figsize=(4,3), dpi=300)
plt.plot(ang,averC,'grey',linewidth=0.1)
# plt.plot(C[0],C[1])
# plt.plot(MS[0],MS[1])
# plt.plot(ZFO[0],ZFO[1])
#FeZn2O4 area

#ZnFe2O4 Area
ZFO_up=0.49835700*40
ZFO_dw=0.28552000*40
plt.axvspan(xmin=ZFO_dw,xmax=ZFO_up,facecolor='grey', alpha=0.2)
#Graphene
plt.axvline(x=0.55477600*40,color='black',alpha=0.6)
#MoSe2
MoSe2_up=0.74719100*40
MoSe2_dw=0.66591400*40
plt.axvspan(xmin=MoSe2_dw,xmax=MoSe2_up,facecolor='grey', alpha=0.2)

plt.axhline(y=0, linestyle='--', color='red', linewidth=1)
# plt.fill_between(ang,averC,where=averC>0,color='red')
# plt.fill_between(ang,averC,where=averC<0,color='blue',alpha=0.7)

# plt.fill_betweenx(averC,ang,1,where=ang<20,color='blue',facecolor='b')
# plt.fill_between(ang,0.5,1,facecolor='green')
# plt.fill_betweenx([0.55477600*40,0.66591400*40],ZFOCM[1]-C[1]-MS[1]-ZFO[1],facecolor='blue')
# plt.xlim(ZFOCM[0].min(),ZFOCM[0].max())
# plt.xlim(8,32)
plt.xlabel("Position along z-axis(Å)")
plt.ylabel('Potential(eV)')
plt.savefig('ZFO_pot', bbox_inches='tight')

print(0.49835700*40)
#C position
print(40*0.55426300)
plt.show()
