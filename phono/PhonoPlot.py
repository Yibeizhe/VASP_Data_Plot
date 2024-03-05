# Created by Junfei Ding at 14:39 2021/05/18
import numpy as np
import os
import re
import matplotlib.pyplot as plt
from matplotlib import rcParams
from shutil import copyfile
# Set times New Times Roman
rcParams['font.family']='serif'
rcParams['font.serif']=['Times New Roman']
# Set spines size
rcParams['axes.linewidth'] =1

class Phono():
    def __init__(self,phon):
        # Use the file name as the name of picture
        self.pic_name=phon.replace('.dat','')

        # np.genfromtxt can remove the empty line in file.
        self.phon=np.genfromtxt(phon)

        # kpoints in each segment are set in band.conf
        # self.segment_kpoints=int(input('Enter K points number, defaut 51: '))
        # if self.segment_kpoints==None:
        self.segment_kpoints=51

        #How many segments in each band?
        with open(phon) as f:
            # The third line in file contains the high symmetry k Points.
            # high symmetry k Points minus 2 is the number of segments
            self.segments=len(f.readlines()[2].split())-2

        # How many k points in each band?
        self.band_kpoints = self.segment_kpoints * self.segments

        # Each k value in every band
        self.k_value = self.phon[0:self.band_kpoints, 0]


    def high_sym_k_name(self):
        print('You need set the high symmetry points name mannually!')
        print('Here I set my defaul value. Change the following line by yourself')
        ksym_name = [r'$\Gamma$', 'M','K', r'$\Gamma$']
        return ksym_name


    def high_sym_k_value(self):
        '''
        Return all the high symmetry points values.
        This can be obtained by comparing the i(th) and i+1(th) k value.
        If they are equal, they must be the high symmetry points.
        '''
        ks = self.k_value
        ksym = []
        ksym.append(ks[0])
        for i in range(len(ks) - 1):
            if ks[i] == ks[i + 1]:
                ksym.append(ks[i])
        ksym.append(ks[-1])
        return ksym


    def phon_plot(self):
        fig = plt.figure(figsize=(4, 3), dpi=300)
        # Get the number of the bands
        n_bands = int(int(self.phon.shape[0]) / self.band_kpoints)

        #Plot each phonon band
        for i in range(n_bands):
            #color='lightseagreen'
            plt.plot(self.k_value, self.phon[i * self.band_kpoints:(i + 1) * self.band_kpoints, 1],
                     linewidth=1.5,color='#1D37A3')

        # Mark the high symmetry k name
        plt.xticks(self.high_sym_k_value(), self.high_sym_k_name(),fontsize=15)
        for i in self.high_sym_k_value():
            plt.axvline(x=i, color='grey', linewidth=0.5, linestyle='--')

        # Set limit of axis
        plt.ylim(self.phon[:, 1].min() - 1, self.phon[:, 1].max() + 1)
        plt.xlim(self.k_value.min(), self.k_value.max())

        # Set label, save figure
        plt.axhline(y=0, linestyle='--', color='red', linewidth=0.5)
        plt.tick_params(direction='in')
        plt.ylabel('Frequency(THz)',fontsize='15')
        # plt.title(self.pic_name,fontsize='12')
        plt.tight_layout()
        # plt.spines.set_linewidth(5)
        fig.savefig(self.pic_name+'.png')
        # plt.show()

def file_list():
    # List all the file in current directory
    files=[]
    file_name = os.listdir(os.getcwd())
    for i in file_name:
        if re.match('[th].*.dat',i):
            files.append(i)
    return files

if __name__ == '__main__':
    files=file_list()
    for i in files:
        print(i)
        j=i.replace("_phon","").replace("_","-")
        j=re.sub('-[345]d','',j)
        copyfile(i,j)
        print(j)
        Phono(j).phon_plot()