import numpy as np
import matplotlib.pyplot as plt
plt.rc('font',family='Times New Roman')
def Potential_plot(potential_file,fermi_level):
    # potential_file=input('Enter the average potential file name: ')
    potential = np.loadtxt(potential_file, comments='#')
    # fermi_level=float(input('Enter the fermi level: '))
    color1 = '#39A1FF'
    color2 = '#FF7F50'
    fig = plt.figure(figsize=(4, 3), dpi=300)
    plt.plot(potential[:, 0], potential[:, 1], color='black', lw=0.5)
    plt.axhline(y=fermi_level, linestyle='--', color='red', linewidth=1.5)
    plt.tick_params(axis='both', direction='in', labelsize=8)
    plt.xlabel("Position along z-axis(Å)")
    plt.ylabel('Effective potential (eV)')
    plt.xlim(potential[:, 0].min(), potential[:, 0].max())
    # plt.xlim(10,35)
    plt.savefig(potential_file+ '.png', bbox_inches='tight')
    plt.show()
if __name__=="__main__":
    files={'CuInP2S6_Ag_Down_PLANAR_AVERAGE.dat':-1.0183,
           'CuInP2S6_Ag_Up_PLANAR_AVERAGE.dat':-0.9351,
           'CuInP2S6_Au_Down_PLANAR_AVERAGE.dat':-1.2816,
           'CuInP2S6_Au_Up_PLANAR_AVERAGE.dat':-1.3461,
           'CuInP2S6_Germanene_down_PLANAR_AVERAGE.dat':-1.7761,
           'CuInP2S6_Germanene_up_PLANAR_AVERAGE.dat':-1.5439,
           'CuInP2S6_Graphene_down_PLANAR_AVERAGE.dat':-1.5546,
           'CuInP2S6_Graphene_up_PLANAR_AVERAGE.dat':-1.2547,
           'CuInP2S6_C-UP_PLANAR_AVERAGE.dat':-1.7366,
           'CuInP2S6_C-Down_PLANAR_AVERAGE.dat':-1.7418}
    ch={'CuInP2S6_C-UP_PLANAR_AVERAGE.dat':-1.7366,
        'CuInP2S6_C-Down_PLANAR_AVERAGE.dat':-1.7418,
        'CuInP2S6_Huang-Down_PLANAR_AVERAGE.dat':-1.7418,
        'CuInP2S6_Huang-UP_PLANAR_AVERAGE.dat':-1.7403}
    Ag_Gr={'CuInP2S6_Ag_Gr_Down_PLANAR_AVERAGE.dat':-0.2567,
           'CuInP2S6_Ag_Gr_Up_PLANAR_AVERAGE.dat':-0.0717}
    Ag_FE12={'CuInP2S6-Ag-FE1_PLANAR_AVERAGE.dat':1.3520,
             'CuInP2S6-Ag-FE2_PLANAR_AVERAGE.dat':1.4374}
    for key,value in Ag_FE12.items():
        print(key,value)
        Potential_plot(key,value)

