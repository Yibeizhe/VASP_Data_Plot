import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.path import Path
from matplotlib.patches import PathPatch
plt.rc('font',family='Times New Roman')
def Potential_plot(potential_file,fermi_level):
    # potential_file=input('Enter the average potential file name: ')
    potential = np.loadtxt(potential_file, comments='#')
    # fermi_level=float(input('Enter the fermi level: '))
    color1 = '#39A1FF'
    color2 = '#FF7F50'
    fig = plt.figure(figsize=(4, 3), dpi=300)
    plt.plot(potential[:, 0], potential[:, 1], color='#1D37A3', lw=1.5)
    plt.axhline(y=fermi_level, linestyle='--', color='red', linewidth=1.5)
    plt.tick_params(axis='both', direction='in', labelsize=8)
    plt.xlabel("Position along z-axis(Å)")
    plt.ylabel('Effective potential (eV)')
    path = Path(np.array([-25*np.ones(potential[:, 0].size),potential[:, 1]]).transpose())
    path=Path(np.array([potential[:, 0],potential[:, 1]]).transpose())
    patch = PathPatch(path, facecolor='none')
    plt.gca().add_patch(patch)
    im = plt.imshow(potential[:, 0].reshape(potential[:, 0].size, 1), cmap=plt.cm.Blues, interpolation="quadric",
                    origin='lower',alpha=0.5,extent=[6, 22, -25,6], aspect="auto", clip_path=patch, clip_on=True)
    # im.set_clip_path(patch)
    # plt.xlim(potential[:, 0].min(), potential[:, 0].max())
    # plt.xlim(10,22)
    plt.savefig(potential_file+ '.png', bbox_inches='tight')
    plt.show()
if __name__=="__main__":
    files={'h-TiN2_Graphene_PLANAR_AVERAGE.dat': -2.7765,
           }
    # ,
    # 'h-TiN2-Cu_PLANAR_AVERAGE.dat': -0.0574
    # 'qu.dat': 2.57794107
    for key,value in files.items():
        print(key,value)
        Potential_plot(key,value)

