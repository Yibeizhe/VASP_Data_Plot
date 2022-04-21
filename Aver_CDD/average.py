import numpy as np
import matplotlib.pyplot as plt
import os
def char_den_diff(hetero,CuInPS='CuInPS.dat',substr='Au.dat'):
    # heterostructure_name="CuInP2S6-Ag-Down.dat"
    hetero_name = hetero.split('.')[0]
    hetero = np.loadtxt(hetero, comments='#')
    # compo1_name='Au.dat'
    compo1= np.loadtxt(CuInPS, comments='#')
    # compo2_name='CuInPS.dat'
    compo2=np.loadtxt(substr,comments='#')
    aver_cdd=hetero[:,1]-compo1[:,1]-compo2[:,1]
    plt.plot(hetero[:,0],aver_cdd)
    plt.axhline(y=0, linestyle='--', color='grey', linewidth=0.7)
    plt.title(hetero_name)
    x1=float(input('x_bottom: '))
    x2 = float(input('x_top: '))
    plt.xlim(x1,x2)
    # plt.plot(interfaces[:,0],interfaces[:,1])
    plt.savefig(hetero_name, figsize=(4, 3), dpi=300, bbox_inches='tight')
    plt.show()


def dirs(direc):
    """
    This function will used to get all the directories which including
    "CuIn" string in its name under "direc" directory.
    """
    dirs = os.listdir(direc)
    pdos_dir = []
    for i in dirs:
        # Judge if the file is a directory and its name including "CuIn"
        if os.path.isdir(i):
            pdos_dir.append(i)
    return pdos_dir

if __name__=="__main__":
    heteros=dirs('.')
    curr_dir=os.getcwd()
    print(heteros)
    for i in heteros:
        os.chdir(i)
        files=os.listdir('.')
        dats=[]
        for j in files:
            if os.path.isfile(j) and '.dat' in j:
                dats.append(j)
        hetero=''
        cuinps=''
        subs=''
        for k in dats:
            if len(k)>10:
                hetero=k
            elif "PS.dat" in k:
                cuinps=k
            else:
                subs=k
        print(hetero,cuinps,subs)
        char_den_diff(hetero,cuinps,subs)
        os.chdir(curr_dir)






