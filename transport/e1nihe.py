import numpy as np
strain=np.array([0.98,0.985,0.99,0.995,1,1.005,1.01,1.015,1.02])-1
cbm=np.array([-4.4419,-4.4615,-4.4846,-4.5018,-4.5225,-4.5454,-4.5707,-4.5875,-4.6104])
e1c=np.polyfit(strain,cbm,1)
e1=np.poly1d(e1c)
print(e1)
def miu(c2d,m1,m2,E1):
    cons_mu=1.6*1.05457**3/(1.38*3*9.109**2*1.6**2)
    mu=cons_mu*c2d/(m1*(m1*m2)**0.5*E1**2)
    return mu
muh=miu(c2d=45.67,m1=0.18,m2=0.19,E1=4.09)
print(muh*10000)