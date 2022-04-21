import numpy as np
import matplotlib.pyplot as plt
import os
plt.rc('font',family='Times New Roman')
def char_den_diff(hetero,CuInPS='CuInPS.dat',substr='Au.dat'):
    # heterostructure_name="CuInP2S6-Ag-Down.dat"
    hetero_name = hetero.split('.')[0]
    hetero = np.loadtxt(hetero, comments='#')
    # compo1_name='Au.dat'
    compo1= np.loadtxt(CuInPS, comments='#')
    # compo2_name='CuInPS.dat'
    compo2=np.loadtxt(substr,comments='#')
    aver_cdd=hetero[:,1]-compo1[:,1]-compo2[:,1]
    return hetero[:,0],aver_cdd

def get_compo(dir):
    """
    Assign the files in 'dir' directory to heterostructure,
    substrate and CuInPS respectively.
    """
    files = os.listdir('.')
    dats = []
    for j in files:
        if os.path.isfile(j) and '.dat' in j:
            dats.append(j)
    hetero = ''
    cuinps = ''
    subs = ''
    for k in dats:
        if len(k) > 10:
            hetero = k
        elif "PS.dat" in k:
            cuinps = k
        else:
            subs = k
    return hetero,cuinps,subs

def open_up_down(dw,up):
    cur_dir=os.getcwd()
    os.chdir(dw)
    dw_compos=get_compo(dw)
    dw_aver=char_den_diff(dw_compos[0],dw_compos[1],dw_compos[2])
    os.chdir(cur_dir)
    os.chdir(up)
    up_compos=get_compo(up)
    up_aver=char_den_diff(up_compos[0],up_compos[1],up_compos[2])
    os.chdir(cur_dir)
    return dw_aver[0],dw_aver[1],up_aver[1]
# distance={'CuInP2S6-Ag_Ag':23.85,'CuInP2S6-Ag_CIPS':26.45}
# distance={'CuInP2S6-Au_Au':23.83,'CuInP2S6-Au_CIPS':26.5}
# distance={'CuInP2S6-Ge_Ge':14.43,'CuInP2S6-Ge_CIPS':17.58}
title='CuInP2S6_Graphene'
# dw_up_aver=open_up_down('CuInP2S6-Ag-down','CuInP2S6-Ag-up')
dw_up_aver=open_up_down('CuInP2S6_Graphene_down','CuInP2S6_Graphene_up')
plt.plot(dw_up_aver[0],dw_up_aver[1],label='FE1')
plt.plot(dw_up_aver[0],dw_up_aver[2],label='FE2')
# plt.axvline(x=23.85, linestyle='--', color='red', linewidth=1)
# plt.axvline(x=26.45, linestyle='--', color='red', linewidth=1)
plt.axhline(y=0, linestyle='--', color='grey', linewidth=1)
plt.xlim(8,24)
plt.xlabel("Position along z-axis(Å)")
plt.ylabel('Electron(e/Å)')
plt.axvspan(xmin=0,xmax=14.43,facecolor='grey', alpha=0.2)
plt.axvspan(xmin=17.85,xmax=30,facecolor='g', alpha=0.2)
plt.legend(loc=1)
plt.savefig(title, figsize=(4, 3), dpi=300, bbox_inches='tight')
plt.show()
