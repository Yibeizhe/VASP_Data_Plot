#!/share/apps/anaconda3/2020.7/bin/python
# Created By Junfei Ding at 2022/09/19
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('AGG')
from matplotlib.pyplot import MultipleLocator
from matplotlib import rcParams
# Set times New Times Roman
plt.rc('font',family='Times New Roman')
# rcParams['font.family']='serif'
# rcParams['font.serif']=['Times New Roman']
class E1C2d():
    """
    Read strain, total energy, vbm, cbm and vaccum level from file.
    The file should have the  following structure:
    strain      energy              vbm         cbm         vacuum-level
    0.980       -52.13569440        -3.7472     -1.8627     1.823
    ...
    """
    def __init__(self,file):
        self.Data_E1=pd.read_table(file,sep='\s+')
        self.strain=self.Data_E1['strain']-1
        self.energy = self.Data_E1['energy']
        self.vac = self.Data_E1['vacuum-level']
        self.vbm = self.Data_E1['vbm'] - self.vac
        self.cbm = self.Data_E1['cbm'] - self.vac
        with open('CONTCAR','r') as f:
            pos=f.readlines()
            # lattice constant a
            self.a=float(pos[2].split()[0])
            # lattice constant b
            self.b=float(pos[3].split()[1])


    def E1vbm(self,x):
        """
        Obtain the hole potential constant, i.e
        The parameter of the fitting linear function of obtain and delta vbm
        """
        e1v = np.polyfit(self.strain, self.vbm, 1)
        E1v = np.poly1d(e1v)
        e1v_fit=np.array([E1v(i) for i in self.strain])
        print(10*"*"+"VBM potential constant"+10*"*")
        # print("The parameters of the fitting curve of strain and vbm energy: ")
        # print(e1v)
        print("Fitting linear function of strain and vbm energy: ")
        print(E1v)
        fig = plt.figure(figsize=(4, 3), dpi=300)
        plt.plot(self.strain,self.vbm,label=x+'-Strain-VBM')
        plt.plot(self.strain,e1v_fit,label=x+'-Strain-VBM-fit')
        plt.legend()
        plt.savefig(x+'-Strain-VBM')
        return e1v[0]


    def E1cbm(self,x):
        """
        Obtain the electron potential constant, i.e
        The parameter of the fitting linear function of obtain and delta cbm
        """
        e1c = np.polyfit(self.strain, self.cbm, 1)
        E1c = np.poly1d(e1c)
        e1c_fit = np.array([E1c(i) for i in self.strain])
        print(10 * "*" + "CBM potential constant" + 10 * "*")
        # print("The parameters of the fitting curve of strain and cbm energy: ")
        # print(e1c)
        print("Fitting linear function of strain and vbm energy: ")
        print(E1c)
        fig = plt.figure(figsize=(4, 3), dpi=300)
        plt.plot(self.strain,self.cbm,label=x+'-Strain-CBM')
        plt.plot(self.strain,e1c_fit,label=x+'-Strain-CBM-fit')
        plt.legend()
        plt.savefig(x+'-Strain-CBM')
        return e1c[0]


    def C2d(self,x):
        """
        Calculating the elasticity modulus, which is the
        second partial derivative of energy with respect to strain
        i.e the coefficient of quadratic term of the quadratic fitting curve
        """
        c2d_p = np.polyfit(self.strain,self.energy,2)
        c2d_poly = np.poly1d(c2d_p)
        c2d_fit = np.array([c2d_poly(i) for i in self.strain])
        # print(10 * "*" + "C2d fitting curve" + 10 * "*")
        # print("The parameters of the fitting curve of strain and total energy: ")
        # print(c2d_p)
        print("Fitting quadratic function of strain and total energy: ")
        print(c2d_poly)
        c2d_p2=c2d_p[0]
        c2d=32*c2d_p2/(self.a*self.b)
        print("The C2d is {} J/m^2.".format(c2d))
        fig = plt.figure(figsize=(4, 3), dpi=300)
        plt.plot(self.strain, self.energy, label=x+'-Strain-Energy')
        plt.plot(self.strain, c2d_fit, label=x+'-Strain-Energy-fit')
        plt.legend()
        plt.savefig(x+'-Strain-Energy')
        return c2d

def mstar(mstar):
    with open(mstar,'r') as f:
        mstar=f.readlines()
        m_v_x=float(mstar[1].split()[1])
        m_v_y=float(mstar[1].split()[2])
        m_c_x=float(mstar[2].split()[1])
        m_c_y=float(mstar[2].split()[2])
    return m_v_y,m_v_x,m_c_y, m_c_x

def miu(c2d,m1,m2,E1):
    cons_mu=1.6*1.05457**3/(1.38*3*9.109**2*1.6**2)
    mu=cons_mu*c2d/(m1*(m1*m2)**0.5*E1**2)
    print("The mobility is {} m2/s/v or {} cm2/s/v".format(mu,mu*10000))
    return mu*10000

def tau(c2d,m1,m2,E1,t):
    cons=2*1.05457**3*32/(3*1.38*9.109*1.6**2)
    rela_t_e=cons*c2d/((m1*m2)**0.5*t*E1**2)
    return rela_t_e

if __name__=="__main__":
    print(30 * '-'+"About VBM(Hole)"+30 * '-')
    m_vbm_y,m_vbm_x,m_cbm_y,m_cbm_x=mstar('mstar.dat')
    print("mstar_vbm_y is {}, mstar_vbm_x is {}.".format(m_vbm_y, m_vbm_x))
    x=E1C2d('E1_x.dat')
    y=E1C2d('E1_y.dat')
    # Obtain the  x,y elasticity modulus.
    C2d_x=x.C2d('x')
    C2d_y=y.C2d('y')
    # Obtain the potential constant
    E1v_x=x.E1vbm('x')
    E1v_y = y.E1vbm('y')

    # About VBM
    mobility_x_vbm=miu(C2d_x,m_cbm_x,m_cbm_y,E1v_x)
    mobility_y_vbm = miu(C2d_y, m_cbm_y, m_cbm_x, E1v_y)

    print("Miu_vbm_x: {}".format(mobility_x_vbm))
    print("Miu_vbm_y: {}".format(mobility_y_vbm))

    # About CBM
    print(30 * '-'+"About CBM(Electron)"+30 * '-')
    E1c_y=y.E1cbm('y')
    E1c_x=x.E1cbm('x')
    mobility_x_cbm=miu(C2d_x,m_cbm_x,m_cbm_y,E1c_x)
    mobility_y_cbm = miu(C2d_y, m_cbm_y, m_cbm_x, E1c_y)

    print("Miu_cbm_x: {}".format(mobility_x_cbm))
    print("Miu_cbm_y: {}".format(mobility_y_cbm))
    print(30 * '-' + "Results summary" + 30 * '-')
    print("Y direction elasticity modulus C2d_y is: {:.3f} J/m^2".format(C2d_y))
    print("X direction elasticity modulus C2d_x is: {:.3f} J/m^2".format(C2d_x))
    print(20 * '-' + "CBM(electron) summary" + 20 * '-')
    print("m*_x_cbm: {:.3f} m0".format(m_cbm_x))
    print("m*_y_cbm: {:.3f} m0".format(m_cbm_y))
    print("E1_x_cbm: {:.3f} eV".format(E1c_x))
    print("E1_y_cbm: {:.3f} eV".format(E1c_y))
    print("Mobility_x_cbm: {:.3f} cm2/s/v".format(mobility_x_cbm))
    print("Mobility_y_cbm: {:.3f} cm2/s/v".format(mobility_y_cbm))
    print(20 * '-' + "VBM(hole) summary" + 20 * '-')
    print("m*_x_vbm: {:.3f} m0".format(m_vbm_x))
    print("m*_y_vbm: {:.3f} m0".format(m_vbm_x))
    print("E1_x_vbm: {:.3f} eV".format(E1v_x))
    print("E1_y_vbm: {:.3f} eV".format(E1v_y))
    print("Mobility_x_vbm: {:.3f} cm2/s/v".format(mobility_x_vbm))
    print("Mobility_y_vbm: {:.3f} cm2/s/v".format(mobility_y_vbm))

    # relaxation time
    print(10*"*"+"The following is the relaxation time"+10*"*")
    t = float(input("The temperature of relaxation time (300K): "))
    tau_x_vbm = tau(C2d_x, m_cbm_x, m_cbm_y, E1v_x,t)
    tau_y_vbm=tau(C2d_y, m_cbm_y, m_cbm_x, E1v_y,t)
    tau_x_cbm=tau(C2d_x,m_cbm_x,m_cbm_y,E1c_x,t)
    tau_y_cbm = tau(C2d_y, m_cbm_x, m_cbm_y, E1c_y,t)
    print("tau_x_vbm: {}".format(tau_x_vbm))
    print("tau_y_vbm: {}".format(tau_y_vbm))
    print("tau_x_cbm: {}".format(tau_x_cbm))
    print("tau_y_cbm: {}".format(tau_y_cbm))
    #Relaxation time
