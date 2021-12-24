#!/share/apps/anaconda3/5.2.0/bin/python
# import matplotlib
#matplotlib.use('AGG')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator
from matplotlib import rcParams
# Set times New Times Roman
plt.rc('font',family='Times New Roman')
# rcParams['font.family']='serif'
# rcParams['font.serif']=['Times New Roman']
class Band():
    def __init__(self, band):
        with open(band) as f:
            self.band = f.readlines()
            # n kpoints in each bands
            self.nks = int(self.band[1].split()[-2])
            # The number of bands
            self.nbands = int(self.band[1].split()[-1])
            print('There are {} bands in {} files '.format(self.nbands,band))
            print('And in each band there are {} kpoints'.format(self.nks))
        self.bands=np.loadtxt(band)
        # K points
        self.kps = self.bands[0:self.nks, 0]


    def band_plot(self,color='grey',la='Total',linewidth=0.5):
        #Use the first band to plot legend
        plt.plot(self.kps,self.bands[0:self.nks,1],linewidth=linewidth, linestyle="-",color=color,label=la)
        for i in range(1,self.nbands):
            # Energy of each band
            energy = self.bands[i * self.nks:(i + 1) * self.nks, 1]
            kpoints = self.bands[i * self.nks:(i + 1) * self.nks, 0]
            plt.plot(kpoints, energy, linewidth=linewidth, linestyle="-", color=color)


    def band_up_down(self,linewidth=1.5,color1='black',color2='red'):
        #plot spin-up
        plt.plot(self.kps,self.bands[0:self.nks,1],linewidth=linewidth, linestyle="-",color=color1,label='UP')
        for i in range(1,self.nbands):
            # Energy of each band
            energy = self.bands[i * self.nks:(i + 1) * self.nks, 1]
            kpoints = self.bands[i * self.nks:(i + 1) * self.nks, 0]
            plt.plot(kpoints, energy, linewidth=linewidth, linestyle="-", color=color1)
        #plot spin-down
        plt.plot(self.kps,self.bands[0:self.nks,2],linewidth=linewidth, linestyle="-",color=color2,label='DW')
        for i in range(1,self.nbands):
            # Energy of each band
            energy = self.bands[i * self.nks:(i + 1) * self.nks, 2]
            kpoints = self.bands[i * self.nks:(i + 1) * self.nks, 0]
            plt.plot(kpoints, energy, linewidth=linewidth, linestyle="-", color=color2)


    def pband_plot(self,color,label):
        for i in range(self.nbands):
            # Energy of each band
            energy = self.bands[i * self.nks:(i + 1) * self.nks, 1]
            # K points of each band
            kpoints = self.bands[i * self.nks:(i + 1) * self.nks, 0]
            plt.scatter(kpoints, energy, self.bands[i * self.nks:(i + 1) * self.nks, 11]**2*50, alpha=0.5,
                        marker='o', color=color, edgecolors=color, linewidths=0.7)
        #The projected legend marker.
        maxindex = np.argmax(self.bands[:,11])
        #Find which band has the maximum projected value
        mp=int(maxindex)//self.nks
        print("The maximum of weight is {}th K point".format(maxindex))
        # energy1=self.bands[mp*self.nks:(mp+1)*self.nks,1]
        # kpoints=self.bands[mp*self.nks:(mp+1)*self.nks,0]
        # plt.scatter(kpoints, energy1, self.bands[mp*self.nks:(mp+1)*self.nks,11], alpha=0.7,
        #             marker='o', color=color, edgecolors=color, linewidths=0.7,label=label)
        plt.scatter(self.bands[maxindex,0],self.bands[maxindex,1],self.bands[maxindex,11]*60, alpha=1,
                    marker='o', color=color, edgecolors=color, linewidths=0.7,label=label)



def k_name_coor(kname='KLABELS',kcoor='KLINES.dat'):
    '''
    Getting the high symmetry K points' name and value from KLABELS and KLINES.dat files,respectively.
    '''
    # Mark the symmetry Kpoints and Fermi level
    # Read the K-points name and coordinates from KLABELS.
    kps = np.loadtxt(kname, dtype='str', skiprows=1, comments="*")
    # The first column is the K high-symmetry points' names.
    k_name = list(kps[:, 0])
    k_name[0]=r'$\Gamma$'
    k_name[-1]=r'$\Gamma$'
    # The K high-symmetry points' coordinates must be read from the KLINES.dat.
    kl = np.loadtxt(kcoor)
    k_coor = np.floor(np.array(sorted(set(kl[:, 0])), dtype=float) * 1000) / 1000
    print('High symmetry K points name are: \n {} \n And Their values are:\n{}\n'.format(k_name,k_coor))
    plt.xticks(k_coor, k_name)
    for i in k_coor:
        plt.axvline(x=i, color='black', linewidth=0.5, linestyle='--', alpha=0.5)


def pband():
    print('Enter the elements needed to be projected')
    elements = input('Note! No more than 5 species: ').split()
    colors = ['blue', 'red', 'green', 'orange', 'cyan']
    pband_datas = []
    spin_or_not=int(input("1) No_Spin projects\n2) Spin projects\n--------->\n"))
    if spin_or_not==1:
        up_dw=''
        for i in range(len(elements)):
            j = 'PBAND_' + elements[i] + '.dat'
            pband_datas.append(j)
    print('****Spin Plot option****')
    if spin_or_not==2:
        up_dw = input("'UP') Spin up projects\n'DW') Spin down projects\n--------->\n")
        for i in range(len(elements)):
            j = 'PBAND_' + elements[i] + '_' + up_dw + '.dat'
            pband_datas.append(j)
    Band(pband_datas[0]).band_plot(la=up_dw,linewidth=0.5)
    for ele in range(len(pband_datas)):
        Band(pband_datas[ele]).pband_plot(color=colors[ele],label=elements[ele])
    # plt.legend(loc='upper right', fontsize=8, framealpha=0.5, frameon=False)
    plt.xlim(Band(pband_datas[0]).kps[0], Band(pband_datas[0]).kps[-1])

if __name__=="__main__":
    fig = plt.figure(figsize=(4,3), dpi=300)
    print('****Band Plot option****')
    band_choose=int(input('1) Total Band\n2) Spin Band\n3) Projected Band\n--------->\n'))
    if band_choose ==1:
        bands = Band('BAND.dat')
        bands.band_plot(linewidth=1.5,color='lightseagreen')
        plt.xlim(bands.kps[0], bands.kps[-1])
    elif band_choose ==2:
        bands = Band('BAND.dat')
        bands.band_up_down()
        plt.xlim(bands.kps[0], bands.kps[-1])
    elif band_choose==3:
        pband()
    else:
        print('Enter wrongly')
    plt.legend(loc='upper right',fontsize=10,framealpha=0.5)
    #Mark the high symmetry points on axis.
    k_name_coor()

    #plot fermi level
    plt.axhline(y=0,linestyle='--',color='red',linewidth=1)

    y_major_locator=MultipleLocator(1)
    ax=plt.gca()
    ax.yaxis.set_major_locator(y_major_locator)
    ylim_b=float(input("Enter the bottom energy: "))
    ylim_t=float(input("Enter the top energy: "))
    plt.ylim(ylim_b,ylim_t)
    tit=input('Enter the title of picture: ')
    plt.title(tit,fontsize=8)
    plt.ylabel('Energy(eV)',fontsize=16)
    plt.tick_params(axis='both',direction='in',labelsize=14)
    figname=input('Enter figure name: ')
    plt.savefig(figname+'.png',bbox_inches='tight')
    plt.show()
