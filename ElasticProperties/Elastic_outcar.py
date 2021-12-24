import matplotlib.pyplot as plt
import numpy as np

#Find the line number of "TOTAL ELASTIC MODULI (kBar)"
# with open('OUTCAR','r') as f:
#     lines=f.readlines()
# for numl,line in enumerate(lines):
#     if "TOTAL ELASTIC MODULI (kBar)" in line:
#         elastic_b=numl
#
# elastic_moduli=[]
# for i in range(elastic_b,elastic_b+10):
#     elastic_moduli.append(lines[i].split())
# print(elastic_moduli)

# c11=float(elastic_moduli[3][1])/10.0
# c12=float(elastic_moduli[3][2])/10.0
# c22=float(elastic_moduli[4][2])/10.0
# c44=float(elastic_moduli[6][4])/10.0
c11=153.763
c12=20.186
c22=195.862
c44=12.855
print('c11: ',c11,' , c12: ',c12,', c22:',c22,' c44: ',c44)
theta=np.linspace(0,2*np.pi,500)
c=np.cos(theta)
s=np.sin(theta)
young_m=(c11*c22-c12**2)/(c11*s**4+c22*c**4+((c11*c22-c12**2)/c44-2*c12)*c**2*s**2)

poisson_r=-((c11+c22-(c11*c22-c12**2)/c44)*c**2*s**2-c12*(s**4+c**4))/(c11*s**4+c22*c**4+((c11*c22-c12**2)/c44-2*c12)*c**2*s**2)

def young_module(theta,young_m):
    fig = plt.figure(figsize=(4, 3), dpi=300)
    plt.polar()
    plt.scatter(theta,young_m,s=0.3*young_m,c=young_m,alpha=1, cmap='RdBu_r')
    plt.colorbar()
    ax=plt.gca()
    ax.set_rmax(young_m.max()*1.1)
    ax.set_rticks(np.arange(0,young_m.max()*1.1,30))  # Less radial ticks
    ax.set_rlabel_position(90,)  # Move radial labels away from plotted line
    ax.grid(True, ls='--', lw=.2, c='k', alpha=.5)
    ax.tick_params(pad=0,labelsize='small',labelcolor='darkblue')
    plt.thetagrids(range(0, 360, 45),fontsize='small')
    # plt.polar(theta,poisson_r)
    plt.title("Young's Modulous",pad=10,fontsize='small')
    plt.savefig('Young_modulous')

def poisson_ratio(theta,poisson_r):
    fig = plt.figure(figsize=(4, 3), dpi=300)
    plt.polar()
    plt.scatter(theta,poisson_r,s=10*poisson_r,c=poisson_r,alpha=1, cmap='RdBu_r')
    plt.colorbar()
    ax=plt.gca()
    ax.set_rmax(poisson_r.max()*1.1)
    ax.set_rticks(np.arange(0,poisson_r.max()*1.1,10))  # Less radial ticks
    ax.set_rlabel_position(90,)  # Move radial labels away from plotted line
    ax.grid(True, ls='--', lw=.2, c='k', alpha=.5)
    ax.tick_params(pad=0,labelsize='small',labelcolor='darkblue')
    plt.thetagrids(range(0, 360, 45),fontsize='small')
    # plt.polar(theta,poisson_r)
    plt.title("CrO2",pad=10,fontsize='small')
    plt.savefig('CrO2')

young_module(theta,young_m)
poisson_ratio(theta,poisson_r)