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
rcParams['axes.linewidth'] =1.5
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
    def tot_plot(self,label='tot',color='grey',ld=0.5):
        plt.plot(self.energy,self.dos_frame['tot'],
                 label=label,color=color,linewidth=ld)

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

def tdos(f,label='Total',color='grey',ld=1):
    with open(f,'r') as tdos:
        tdos_name=tdos.readlines()[0].split()
    tdosdata=np.loadtxt(f)
    energy=tdosdata[:,0]
    dos=tdosdata[:,1]
    plt.plot(energy,dos,label=label,color=color,linewidth=1,alpha=0.1)
    plt.fill(energy, dos, color=color, alpha=0.1)

def MoSe2_MoO2_Graphene():
    # MoO2_Mo = Dosplot('PDOS_MoO2-Mo.dat')
    # MoO2_Mo.tot_plot(label='MoO$_{2}$-Mo',color='#1D37A3',ld=1.5)
    MoSe2_Mo = Dosplot('PDOS_Mo.dat')
    MoSe2_Mo.tot_plot(label='Mo',color='red',ld=1.5)
    C = Dosplot('PDOS_C.dat')
    C.tot_plot(label='C',color='blue',ld=1.5)
    Se= Dosplot('PDOS_Se.dat')
    Se.tot_plot(label='Se',color='brown',ld=1.5)

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
    y_major=MultipleLocator(40)
    x_major=MultipleLocator(1)
    ax.yaxis.set_major_locator(y_major)
    ax.xaxis.set_major_locator(x_major)
    # mdn2p(metal='Ti')
    tdos('TDOS.dat')
    MoSe2_MoO2_Graphene()
    # Cu_layer()
    plt.xlabel('Energy(eV)',fontsize=16,fontweight='bold', fontstyle='italic')
    # plt.ylabel('DOS',fontsize=20)
    plt.axhline(y=0, linestyle='--', color='grey', linewidth=0.7)
    plt.axvline(x=0, linestyle='--', color='red', linewidth=1)
    # plt.legend(loc='upper right',fontsize=12)
    # plt.title('h-Ti'+'$N_2$',fontsize=20)
    plt.tick_params(direction='in',labelsize=16)
    plt.xlim(-3,2)
    plt.ylim(0,80)
    plt.savefig('MoSe-Graphene_PDOS', figsize=(4, 3), dpi=600, bbox_inches='tight')
    plt.show()



