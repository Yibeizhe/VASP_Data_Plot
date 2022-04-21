import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
plt.rc('font',family='Times New Roman')
def Potential_plot(potential_file,fermi_level):
    # potential_file=input('Enter the average potential file name: ')
    potential = np.loadtxt(potential_file, comments='#')
    # fermi_level=float(input('Enter the fermi level: '))
    color1 = '#39A1FF'
    color2 = '#FF7F50'
    fermi_uplift=0-float(fermi_level)
    #Uplift Fermi level to 0 eV
    energy=potential[:,1]+fermi_uplift
    return potential[:,0], energy

files={'CuInP2S6_Ag_Down_PLANAR_AVERAGE.dat':-1.0183,
       'CuInP2S6_Ag_Up_PLANAR_AVERAGE.dat':-0.9351,
       'CuInP2S6_Huang-Down_PLANAR_AVERAGE.dat': -1.7418,
       'CuInP2S6_Huang-UP_PLANAR_AVERAGE.dat': -1.7403,
       'CuInP2S6_Germanene_down_PLANAR_AVERAGE.dat': -1.7761,
       'CuInP2S6_Germanene_up_PLANAR_AVERAGE.dat': -1.5439,
       'CuInP2S6_Graphene_down_PLANAR_AVERAGE.dat': -1.5546,
       'CuInP2S6_Graphene_up_PLANAR_AVERAGE.dat': -1.2547,
       'CuInP2S6_Ag_Gr_Down_PLANAR_AVERAGE.dat': -0.2567,
       'CuInP2S6_Ag_Gr_Up_PLANAR_AVERAGE.dat': -0.0717
       }
distans={'Au':[23.9,26.5],'Gr':[14.43,17.82],
         'Ag':[12.0,14.64],'Ge':[14.4,17.64],
         'Ag-Gr':[26.7,30.05]}

Au_dw=Potential_plot('CuInP2S6_Huang-Down_PLANAR_AVERAGE.dat', -1.7418)
Au_up=Potential_plot('CuInP2S6_Huang-UP_PLANAR_AVERAGE.dat',-1.7403)
Ag_dw=Potential_plot('CuInP2S6-Ag-FE1_PLANAR_AVERAGE.dat',1.3520)
Ag_up=Potential_plot('CuInP2S6-Ag-FE2_PLANAR_AVERAGE.dat',1.4374)
Gr_dw=Potential_plot('CuInP2S6_Graphene_down_PLANAR_AVERAGE.dat', -1.5546)
Gr_up=Potential_plot('CuInP2S6_Graphene_up_PLANAR_AVERAGE.dat', -1.2547)
Ge_dw=Potential_plot('CuInP2S6_Germanene_down_PLANAR_AVERAGE.dat',-1.7761)
Ge_up=Potential_plot('CuInP2S6_Germanene_up_PLANAR_AVERAGE.dat',-1.5439)
Ag_Gr_dw=Potential_plot('CuInP2S6_Ag_Gr_Down_PLANAR_AVERAGE.dat', -0.2567)
Ag_Gr_up=Potential_plot('CuInP2S6_Ag_Gr_Up_PLANAR_AVERAGE.dat', -0.0717)

fig = plt.figure(figsize=(4, 3), dpi=300)
plt.plot(Ag_Gr_dw[0],Ag_Gr_dw[1],label='FE1',linewidth=0.7)
plt.plot(Ag_Gr_up[0],Ag_Gr_up[1],label='FE2',color='red',linewidth=0.7)
plt.axhline(y=0, linestyle='--', color='red', linewidth=0.5)
plt.tick_params(axis='both', direction='in', labelsize=6)
plt.xlabel("Position along z-axis(Å)",fontsize=7)
plt.ylabel('Effective potential (eV)',fontsize=7)
plt.axvspan(xmin=0,xmax=26.7,facecolor='grey', alpha=0.2)
plt.axvspan(xmin=30.05,xmax=50,facecolor='g', alpha=0.2)
# plt.xlim(Gr_Gr_up[0].min(), Gr_Gr_up[0].max())
# plt.xlim(10,24)
ax=plt.gca()
ax.xaxis.set_major_locator(MultipleLocator(2))
plt.legend(loc=1,fontsize=6)
plt.xlim(12,38)
plt.savefig('CuInP2S6_Ag_Gr-up-down'+ '.png', bbox_inches='tight')
plt.show()
