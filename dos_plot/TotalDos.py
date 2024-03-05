import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import rcParams
from matplotlib.pyplot import MultipleLocator
plt.rc('legend', fontsize=7)
rcParams['font.family']='serif'
rcParams['font.serif']=['Times New Roman']
rcParams['axes.linewidth'] =1
def fileopen(f,color="#1D37A3"):
    dos_data = np.loadtxt(f)
    # Energy
    energy = dos_data[:, 0]
    dos = dos_data[:, 1]
    plt.plot(energy, dos,color=color,label='DOS')
    ax = plt.gca()
    # y_major = MultipleLocator(1.2)
    # x_major = MultipleLocator(1)
    # ax.yaxis.set_major_locator(y_major)
    # ax.xaxis.set_major_locator(x_major)
    plt.xlabel('Energy(eV)', fontsize=20)
    # plt.ylabel('DOS',fontsize=20)
    plt.axhline(y=0, linestyle='--', color='grey', linewidth=0.7)
    plt.axvline(x=0, linestyle='--', color='red', linewidth=1)
    plt.legend(loc='upper right', fontsize=10)
    # plt.title('DOS', fontsize=20)
    plt.tick_params(direction='in', labelsize=15)
    # plt.ylim(0, np.max(dos))
    plt.ylim(0, 100)
    plt.xlim(-2,2)
    file_name=f.split('.')[0]

    plt.savefig(file_name, figsize=(3,4),dpi=300,bbox_inches='tight')
    plt.show()
    # plt.ylim(0,100    )

fileopen('MoO2-MoSe-Graphene-TDOS.dat')
# if __name__=="main":
