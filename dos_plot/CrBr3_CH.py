import matplotlib.pyplot as plt
import os
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
class DosPlot():
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
        # t2g state dxy+dyz+dxz
        self.dos_t2g=self.dos_frame['dxy']+self.dos_frame['dyz']+self.dos_frame['dxz']
        # eg state dx2+dz2
        self.dos_eg=self.dos_frame['dx2']+self.dos_frame['dz2']
        #Difine the plotting color
        self.colors = ['blue', 'orange', 'green', 'red', 'purple',
                  'brown', 'pink', 'grey', 'olive', 'cyan']

    #pdos=pz+px+py
    def pdos(self):
        p=self.dos_frame['pz']+self.dos_frame['px']+self.dos_frame['py']
        return p

    #ddos
    def ddos(self):
        d=self.dos_frame['dxy']+self.dos_frame['dyz']+\
              self.dos_frame['dz2']+self.dos_frame['dxz']+self.dos_frame['dx2']
        return d

    #t2g
    def t2g(self):
        t2g=self.dos_frame['dxy']+self.dos_frame['dyz']+self.dos_frame['dxz']
        return t2g

    #eg
    def eg(self):
        eg=self.dos_frame['dx2'] + self.dos_frame['dz2']
        return eg

    # Plot the total dos
    def dos_plot(self,color='black',label='total'):
        plt.plot(self.energy,self.dos_data[:,1],label=label,
                 color=color)

    # tot plot
    def tot_plot(self,label='tot',color='grey'):
        plt.plot(self.energy,self.dos_frame['tot'],
                 label=label,color=color,linewidth='0.5')

    # Plot spin total dos
    def spin_dos_plot(self,color='black',label='total'):
        plt.plot(self.energy,self.dos_data[:,1],color=color,label=label)
        plt.plot(self.energy, self.dos_data[:, 2],color=color)

    #Plot s dos
    def s_plot(self,s='s',s_color='black',ld=1):
        plt.plot(self.energy, self.dos_frame['s'],
                 label=s, color=s_color, linewidth=ld)

    # plot p=px+py+pz state
    def p_plot(self,p='p',cp='blue',ld=0.5):
        plt.plot(self.energy,self.pdos(),label=p,color=cp,linewidth=ld)
        plt.fill(self.energy,self.pdos(), color=cp, alpha=0.3)

    # plot d=dxy+dyz+... state
    def d_plot(self,d='d',cd='red',ld=0.5):
        d_dos=self.dos_frame['dxy']+self.dos_frame['dyz']+\
              self.dos_frame['dz2']+self.dos_frame['dxz']+self.dos_frame['dx2']
        plt.plot(self.energy,d_dos,label=d,color=cd,linewidth=ld)
        plt.fill(self.energy, d_dos, color=cd, alpha=0.1)

    # Plot the px, py, pz respectively.
    def pxyz_plot(self):
        for i in range(2,5):
            plt.plot(self.energy,self.dos_data[:,i],
                     color=self.colors[i-2])
    # Plot the dx, dy, ...,dx2
    def dxyz_plot(self,ld=0.5):
        for i in range(5,10):
            plt.plot(self.energy,self.dos_data[:,i],
                     color=self.colors[i-5],linewidth=ld)

    # Plot whatever you want.
    def want_plot(self,ld=0.5):
        print(self.dos_frame.keys())
        print('The states in your dos files is as following:\n',self.dos_name)
        x=input('Which state you want to plot?\n------>\n').split()
        x='dxy dyz dz2 dxz dx2'.split()
        for i,j in enumerate(x):
            plt.plot(self.energy,self.dos_frame[j],label=j,color=self.colors[i],
                     linewidth=ld)

    #Plot t2g and eg
    def t2g_eg_plot(self,color_2g='blue',color_eg='royalblue',label1='',label2='',lw=1):
        plt.plot(self.energy,self.dos_t2g,color=color_2g,label=label1,linewidth=lw)
        plt.plot(self.energy,self.dos_eg,color=color_eg,label=label2,linewidth=lw)

def Cr_d(direc):
    # About metal d spin down
    cr_dw = DosPlot(direc+'PDOS_Cr_DW.dat')
    cr_dw.t2g_eg_plot(label1='$Cr-t_{2g}$',label2='$Cr-e_{g}$',lw=0.5)
    # About metal d spin up
    cr_up = DosPlot(direc+'PDOS_Cr_UP.dat')
    cr_up.t2g_eg_plot(lw=0.5)

def CrX3_C(direc,X='X'):
    #About n 2p spin down
    c_dw = DosPlot(direc+'PDOS_C_DW.dat')
    # c_dw.p_plot(p='$C_{2p}$')
    c_dw.tot_plot(color='black',label='C')

    # About n 2p spin up
    c_up = DosPlot(direc+'PDOS_C_UP.dat')
    # c_up.p_plot(p='')
    c_up.tot_plot(color='black',label='')

    #About n 2p spin down
    x_dw = DosPlot(direc+'PDOS_Br_DW.dat')
    # x_dw.p_plot(p='$Br_{p}$')
    x_dw.tot_plot(color='green',label='Br')

    # About n 2p spin up
    x_up = DosPlot(direc+'PDOS_Br_UP.dat')
    # x_up.p_plot(p='')
    x_up.tot_plot(color='green',label='')

    # # About metal d spin down
    # cr_dw = DosPlot('PDOS_{}_DW.dat'.format(X))
    # # cr_dw.d_plot(d=X+'${}_{d}$')
    # cr_dw.tot_plot(color='red',label='')
    #
    # # About metal d spin up
    # cr_up = DosPlot('PDOS_{}_UP.dat'.format(X))
    # # cr_dw.d_plot(d=X+'${}_{d}$')
    # cr_up.tot_plot(color='red',label='Cr')

if __name__=="__main__":
    fig = plt.figure(figsize=(4, 3), dpi=300)
    # Cr_d('CrBr3_6CH_Br_oct')
    ax=plt.gca()
    direct='CrBr3_GBs1/'
    Cr_d(direct)
    CrX3_C(direct)
    # y_major=MultipleLocator(1.2)
    # x_major=MultipleLocator(1)
    # ax.yaxis.set_major_locator(y_major)
    # ax.xaxis.set_major_locator(x_major)
    plt.xlabel('Energy(eV)',fontsize=12)
    # plt.ylabel('DOS',fontsize=20)
    plt.axhline(y=0, linestyle='--', color='grey', linewidth=0.7)
    plt.axvline(x=0, linestyle='--', color='red', linewidth=1)
    plt.legend(loc='upper right',fontsize=6)
    plt.title('CrBr'+'$_3$'+'-57CH',fontsize=12)
    plt.tick_params(direction='in',labelsize=12)
    # plt.xlim(-4,4)
    # plt.ylim(-10,10)
    plt.savefig('CrBr3_57CH_Br-7Ring_oct', bbox_inches='tight')
    plt.show()