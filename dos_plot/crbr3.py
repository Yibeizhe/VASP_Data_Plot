from DosPlot import Dosplot as dp
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import os

crbr3 = 'CrBr3_oct/'
cr_dw = dp(crbr3 + 'PDOS_Cr_DW.dat')
cr_up = dp(crbr3 + 'PDOS_Cr_UP.dat')
br_up=dp(crbr3+'PDOS_Br_UP.dat')
br_dw = dp(crbr3 +'PDOS_Br_DW.dat')


crbr_c_l=['CrBr3_57CH_Br-7Ring_oct','CrBr3_66CH_Br_oct',
          'CrBr3_GB2_oct','CrBr3_6CH_Br_oct',
          'CrBr_Gr_oct','CrBr3_GB1_oct','Azul@CrI3','Ben@CrI3','Naph@CrI3']

crbr_ch='Naph@CrI3'
crbr_c=crbr_ch+'/'
crc_up=dp(crbr_c+'PDOS_Cr_UP.dat')
crc_dw = dp(crbr_c + 'PDOS_Cr_DW.dat')
brc_up=dp(crbr_c+'PDOS_I_UP.dat')
brc_dw = dp(crbr_c +'PDOS_I_DW.dat')
cc_up=dp(crbr_c+'PDOS_C_UP.dat')
cc_dw=dp(crbr_c+'PDOS_C_DW.dat')

plt.figure(figsize=(4,3),dpi=300)
al=0.7
ld=2
plt.plot(crc_up.energy,crc_dw.t2g(),color='#0098DA',
         linewidth=ld,label='$Cr-t_{2g}$')
plt.fill(crc_up.energy,crc_dw.t2g(),color='#0098DA', alpha=al)
plt.plot(crc_up.energy,crc_dw.eg(),color='#94CBED',
         linewidth=ld,label='$Cr-e_g$')
plt.fill(crc_up.energy,crc_dw.eg(),color='#94CBED',alpha=al)
plt.plot(crc_up.energy,crc_up.t2g(),color='#0098DA',
         linewidth=ld)
plt.fill(crc_up.energy,crc_up.t2g(),color='#0098DA',alpha=al)
plt.plot(crc_up.energy,crc_up.eg(),color='#94CBED',
         linewidth=ld)
plt.fill(crc_up.energy,crc_up.eg(),color='#94CBED',alpha=al)

#Plot CrBr3_CH-Br
plt.plot(brc_up.energy,brc_up.pdos(),color='limegreen',
         linewidth=ld,label='$Br_p$')
plt.plot(brc_up.energy,brc_dw.pdos(),color='limegreen',
         linewidth=ld)
# Plot CrBr3_CH-C
plt.plot(cc_up.energy,cc_up.pdos(),color='black',
         linewidth=ld,label='$C_p$')
plt.plot(cc_up.energy,cc_dw.pdos(),color='black',
         linewidth=ld)

plt.axhline(y=0, linestyle='--', color='grey', linewidth=0.5)
plt.axvline(x=0, linestyle='--', color='red', linewidth=0.5)
plt.xlim(-4, 3)
plt.ylim(-30, 30)
y_major = MultipleLocator(30)
x_major = MultipleLocator(1)
ax=plt.gca()
ax.yaxis.set_major_locator(y_major)
ax.xaxis.set_major_locator(x_major)
plt.legend(loc='upper right',fontsize=6)
plt.xlabel('Energy(eV)')
plt.tick_params(direction='in')
plt.savefig(crbr_ch, dpi=300, bbox_inches='tight')
plt.show()
