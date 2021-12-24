#!/share/apps/anaconda3/5.2.0/bin/python
# import matplotlib
#matplotlib.use('AGG')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

class HseBand():
    def __init__(self,hse='BAND.dat',kname='KLABELS'):
        self.hseband=np.genfromtxt(hse)
        self.kps = np.loadtxt(kname, dtype='str', skiprows=1, comments="*")
        with open(hse,'r') as band:
            line1 = band.readlines()[1].split()
            self.nkps=int(line1[4])
            self.nbands=int(line1[5])
        self.ks=self.hseband[0:1*self.nkps,0]

    def ksym_value(self):
        '''
        Return all the high symmetry points values.
        This can be obtained by comparing the i(th) and i+1(th) k value.
        If they are equal, they must be the high symmetry points.
        '''
        ks = self.hseband[0:1*self.nkps,0]
        ksym = []
        ksym.append(self.ks[0])
        for i in range(len(self.ks) - 1):
            if self.ks[i] == self.ks[i + 1]:
                ksym.append(self.ks[i])
        ksym.append(self.ks[-1])
        return ksym

    def k_name(self):
        '''
        Getting the high symmetry K points' name and value from KLABELS files.
        '''
        # Read the K-points name and coordinates from KLABELS.
        # The first column is the K high-symmetry points' names.
        k_name = list(self.kps[:, 0])
        k_name[0] = r'$\Gamma$'
        k_name[-1] = r'$\Gamma$'
        return k_name


    def ksym_tick_plot(self):
        plt.xticks(self.ksym_value(),self.k_name())
        for i in self.ksym_value():
            plt.axvline(x=i, color='black', linewidth=0.5, linestyle='--', alpha=0.5)


    def hseplot(self,linewidth=1.5,color='lightseagreen',la=''):
        #Use the first band to plot band legend
        plt.plot(self.ks, self.hseband[0:self.nkps, 1],
                 linewidth=linewidth, linestyle="-", color=color, label=la)
        for i in range(1,self.nbands):
            plt.plot(self.hseband[i*self.nkps:(i+1)*self.nkps,0],
                     self.hseband[i*self.nkps:(i+1)*self.nkps,1],
                     linewidth=linewidth, linestyle="-", color=color)
        self.ksym_tick_plot()


    def hse_spin_plot(self,linewidth=1.5,color1='black',color2='red'):
        #plot spin-up
        plt.plot(self.hseband[0:1*self.nkps,0],self.hseband[0:self.nkps,1],
                 linewidth=linewidth, linestyle="-",color=color1,label='UP')
        for i in range(1,self.nbands):
            # Energy of each band
            energy = self.hseband[i * self.nkps:(i + 1) * self.nkps, 1]
            kpoints = self.hseband[i * self.nkps:(i + 1) * self.nkps, 0]
            plt.plot(kpoints, energy, linewidth=linewidth, linestyle="-", color=color1)
        #plot spin-down
        plt.plot(self.hseband[0:1*self.nkps,0],self.hseband[0:self.nkps,2],
                 linewidth=linewidth, linestyle="-",color=color2,label='DW')
        for i in range(1,self.nbands):
            # Energy of each band
            energy = self.hseband[i * self.nkps:(i + 1) * self.nkps, 2]
            kpoints = self.hseband[i * self.nkps:(i + 1) * self.nkps, 0]
            plt.plot(kpoints, energy, linewidth=linewidth, linestyle="-", color=color2)

if __name__=="__main__":
    fig = plt.figure(figsize=(3, 4), dpi=300)
    hse=HseBand()
    hse.ksym_tick_plot()
    band_choose=int(input('1) HSE Band\n2) HSE_SPIN Band\n--------->\n'))
    if band_choose ==1:
        hse.hseplot()
    elif band_choose ==2:
        hse.hse_spin_plot()
    else:
        print('Enter wrongly')
    plt.legend(loc='upper right', fontsize=8, framealpha=0.5)
    # plot fermi level
    plt.axhline(y=0, linestyle='--', color='red', linewidth=1)

    y_major_locator = MultipleLocator(1)
    ax = plt.gca()
    ax.yaxis.set_major_locator(y_major_locator)
    ylim_b = float(input("Enter the bottom energy: "))
    ylim_t = float(input("Enter the top energy: "))
    plt.ylim(ylim_b, ylim_t)
    plt.xlim(hse.ks.min(), hse.ks.max())
    tit = input('Enter the title of picture: ')
    plt.title(tit, fontsize=8)
    plt.ylabel('Energy(eV)', fontsize=8)
    plt.tick_params(axis='both', direction='in', labelsize=8)
    figname = input('Enter figure name: ')
    plt.savefig(figname + '.png', bbox_inches='tight')

