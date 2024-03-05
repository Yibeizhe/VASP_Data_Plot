import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import re
import os
# Set times New Times Roman
rcParams['font.family']='serif'
rcParams['font.serif']=['Times New Roman']
rcParams['axes.linewidth'] =1.5
def plot_md(mdfile,label,title):
    md=np.loadtxt(mdfile)
    time_md=md[:,0]
    energy=md[:,1]
    fig, ax = plt.subplots()
    ax.plot(time_md,energy,linewidth=2,color='#1D37A3',label=label)
    plt.xlim(0,time_md.max())
    plt.xlabel('Time(fs)',fontsize=15)
    plt.ylim(energy.min()-10,energy.max())
    plt.ylabel('Energy(eV)',fontsize=15)
    ax.tick_params(labelcolor='black', labelsize='x-large', width=3)
    pic_name=mdfile.replace('.dat','')
    # plt.title(pic_name)
    plt.tick_params(direction='in')
    # plt.title(title,fontsize=10)
    ax.legend(loc='upper right',prop = {'size':15})
    fig.savefig(pic_name,figsize=(3, 3), dpi=300,bbox_inches='tight')
    plt.tight_layout()

def file_list():
    # List all the file in current directory
    files=[]
    file_name = os.listdir(os.getcwd())
    for i in file_name:
        if re.match('[th].*.dat',i):
            files.append(i)
    return files

if __name__ == '__main__':
    mdfiles=file_list()
    for i in mdfiles:
        print(i)
        pic_title=str(i).replace('.dat','')
        plot_md(str(i),label='500K',title=pic_title)
