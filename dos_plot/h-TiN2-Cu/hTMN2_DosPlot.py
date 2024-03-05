import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import rcParams
from matplotlib.pyplot import MultipleLocator
# from matplotlib.font_manager import FontProperties
# Set times New Times Roman
# plt.rcParams.update({'font.size': 5})
plt.rc('legend', fontsize=7)
rcParams['font.family']='serif'
rcParams['font.serif']=['Times New Roman']
rcParams['axes.linewidth'] =1
class Dosplot():
    def __init__(self,dos):
        # Get the dos name namel  s p dx dxy...
        with open(dos,'r') as dosfile:
            self.dos_name=dosfile.readlines()[0].split()
        self.dos_data=np.loadtxt(dos)
        # Energy
        self.energy=self.dos_data[:,0]
        # Decide how many columns in dos file
        self.dos_columns = self.dos_data.shape[1]
        # Energy maximum
        self.me=self.energy.max()
        # Energy minimum
        self.ne=self.energy.min()
        # put the dos file in pandas DataFrame
        self.dos_frame=pd.DataFrame(self.dos_data,columns=self.dos_name)
        #Difine the plotting color
        self.colors = ['blue', 'orange', 'green', 'red', 'purple',
                  'brown', 'pink', 'grey', 'olive', 'cyan']

    # pdos=pz+px+py
    def pdos(self):
        p = self.dos_frame['pz'] + self.dos_frame['px'] + self.dos_frame['py']
        return p

    # ddos
    def ddos(self):
        d = self.dos_frame['dxy'] + self.dos_frame['dyz'] + \
            self.dos_frame['dz2'] + self.dos_frame['dxz'] + self.dos_frame['dx2']
        return d

    # t2g
    def t2g(self):
        t2g = self.dos_frame['dxy'] + self.dos_frame['dyz'] + self.dos_frame['dxz']
        return t2g

    # eg
    def eg(self):
        eg = self.dos_frame['dx2'] + self.dos_frame['dz2']
        return eg

    # Plot the total dos
    def dos_plot(self,color='black',label='total'):
        plt.plot(self.energy,self.dos_data[:,1],label=label,
                 color=color)

    # Plot spin total dos
    def spin_dos_plot(self,color='black',label='total'):
        plt.plot(self.energy,self.dos_data[:,1],color=color,label=label)
        plt.plot(self.energy, self.dos_data[:, 2],color=color)

    #Plot s dos
    def s_plot(self,s='s',s_color='black',ld=1):
        plt.plot(self.energy, self.dos_frame['s'],
                 label=s, color=s_color, linewidth=ld)

    # plot p=px+py+pz state
    def p_plot(self,p='p',cp='#FDB4B6',ld=1.5):
        plt.plot(self.energy,self.pdos(),label=p,color=cp,linewidth=ld)
        plt.fill(self.energy,self.pdos(), color=cp, alpha=0.3)

    # plot d=dxy+dyz+... state
    def d_plot(self,d='d',cd='#1D37A3',ld=1.5):
        plt.plot(self.energy,self.ddos(),label=d,color=cd,linewidth=ld)
        plt.fill(self.energy, self.ddos(), color=cd, alpha=0.1)

    # tot plot
    def tot_plot(self,label='tot',color='grey'):
        plt.plot(self.energy,self.dos_frame['tot'],
                 label=label,color=color,linewidth='0.5')

    # Plot the px, py, pz respectively.
    def pxyz_plot(self):
        for i in range(2,5):
            plt.plot(self.energy,self.dos_data[:,i],
                     color=self.colors[i-2])
    # Plot the dx, dy, ...,dx2
    def dxyz_plot(self):
        for i in range(5,10):
            plt.plot(self.energy,self.dos_data[:,i],
                     color=self.colors[i-5])

    # Plot whatever you want.
    def want_plot(self):
        print(self.dos_frame.keys())
        print('The states in your dos files is as following:\n',self.dos_name)
        x=input('Which state you want to plot?\n------>\n').split()
        for i,j in enumerate(x):
            plt.plot(self.energy,self.dos_frame[j],label=j,color=self.colors[i])

    #Plot t2g and eg
    def t2g_eg_plot(self,c_2g='blue',l_2g='$t_{2g}$',l_eg='$e_g$',c_eg='skyblue',lw=0.5,ltype=':'):
        plt.plot(self.energy,self.t2g(),color=c_2g,
                 linewidth=lw,linestyle=ltype,label=l_2g)
        plt.plot(self.energy,self.eg(),color=c_eg,
                 linewidth=lw,linestyle=ltype,label=l_eg)

def metal_spd(metal="Ti"):
    m_up = Dosplot('PDOS_{}_UP.dat'.format(metal))
    m_up.s_plot()
    m_up.p_plot()
    m_up.d_plot()
    m_up.tot_plot(label='$Ti_{total}$')

def Cu_layer():
    # cu1=Dosplot('PDOS_Cu_1layer.dat')
    # cu1.tot_plot(color='#deb887',label='Cu1')
    # cu2=Dosplot('PDOS_Cu_2layer.dat')
    # cu2.tot_plot(color='#f5f5dc',label='Cu2')
    # cu3=Dosplot('PDOS_Cu_3layer.dat')
    # cu3.tot_plot(color='#ffe4c4',label='Cu3')
    cu4=Dosplot('PDOS_Cu_4layer.dat')
    # cu4.tot_plot(color='lightseagreen',label='Cu4')
    cu4.d_plot(cd='lightseagreen', d='Cu4')


def N_sp(metal):
    n_up = Dosplot('PDOS_N_UP.dat'.format(metal))
    n_up.s_plot()
    n_up.p_plot()
    n_up.tot_plot(label='$N_{total}$')

def mdn2p(metal):
    metal="Ti"
    # About n 2p spin up
    n_up = Dosplot('PDOS_N.dat'.format(metal))
    n_up.p_plot(p='$N_{2p}$')
    # n_up.tot_plot(color='blueviolet',label='$N_{total}$')

    # About metal d spin up
    m_up = Dosplot('PDOS_Ti.dat')
    m_up.d_plot(d='$Ti_{3d}$')
    # m_up.tot_plot(color='darkred',label=metal+'$_{total}$')

    Cu_C=Dosplot('PDOS_Cu_4layer.dat')
    Cu_C.d_plot(d='$Cu_{3d}$',cd='lightseagreen')
if __name__=="__main__":
    #Pictures setting
    fig = plt.figure(figsize=(4, 3), dpi=300)
    ax=plt.gca()
    # y_major=MultipleLocator(1.2)
    # x_major=MultipleLocator(1)
    # ax.yaxis.set_major_locator(y_major)
    # ax.xaxis.set_major_locator(x_major)
    mdn2p(metal='Ti')
    # Cu_layer()
    plt.xlabel('Energy(eV)',fontsize=20)
    # plt.ylabel('DOS',fontsize=20)
    plt.axhline(y=0, linestyle='--', color='grey', linewidth=0.7)
    plt.axvline(x=0, linestyle='--', color='red', linewidth=1)
    plt.legend(loc='upper right',fontsize=10)
    # plt.title('h-Ti'+'$N_2$',fontsize=20)
    plt.tick_params(direction='in',labelsize=15)
    plt.xlim(-2,2)
    plt.ylim(0,10)
    plt.savefig('h-{}N2-Cu'.format("Ti"), figsize=(6, 2), dpi=300, bbox_inches='tight')
    # plt.show()



