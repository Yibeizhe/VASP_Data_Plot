import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Set New Times Roman font for plotting
from matplotlib import rcParams
rcParams['font.family']='serif'
rcParams['font.serif']=['Times New Roman']
def young_module(theta,young_m,title='Young_modulous'):
    fig = plt.figure(figsize=(4, 3), dpi=300)
    plt.polar()
    plt.scatter(theta,young_m,s=0.005*young_m**2,c=young_m,alpha=1, cmap='RdBu_r')
    plt.colorbar()
    ax=plt.gca()
    ax.set_rmax(young_m.max()*1.1)
    ax.set_rticks(np.arange(0,young_m.max()*1.1,20))  # Less radial ticks
    ax.set_rlabel_position(90,)  # Move radial labels away from plotted line
    ax.grid(True, ls='--', lw=.2, c='k', alpha=.5)
    ax.tick_params(pad=0,labelsize='small',labelcolor='darkblue')
    plt.thetagrids(range(0, 360, 45),fontsize='small')
    # plt.polar(theta,poisson_r)
    plt.title("Young Modulous (N/m)",pad=10,fontsize='small')
    plt.savefig(title)

def poisson_ratio(theta,poisson_r,title='Poisson_Ratio'):
    fig = plt.figure(figsize=(4, 3), dpi=300)
    plt.polar()
    plt.scatter(theta,poisson_r,s=10*poisson_r,c=poisson_r,alpha=1, cmap='RdBu_r')
    plt.colorbar()
    ax=plt.gca()
    ax.set_rmax(poisson_r.max()*1.1)
    ax.set_rticks(np.arange(0,poisson_r.max()*1.1,0.1))  # Less radial ticks
    ax.set_rlabel_position(90,)  # Move radial labels away from plotted line
    ax.grid(True, ls='--', lw=.2, c='k', alpha=.5)
    ax.tick_params(pad=0,labelsize='small',labelcolor='darkblue')
    plt.thetagrids(range(0, 360, 45),fontsize='small')
    # plt.polar(theta,poisson_r)
    plt.title("Poisson Ratio",pad=10,fontsize='small')
    plt.savefig(title)

c11=115.085

c12=63.81
c44=25.638
# c11=117.0
# c12=17.4
# c44=26.1
c22=c11
i="tetra-MnN2"
# print(i)
# print(c11,c22,c12,c44)
theta = np.linspace(0, 2 * np.pi, 500)
c = np.cos(theta)
s = np.sin(theta)
young_m = (c11 * c22 - c12 ** 2) / (
            c11 * s ** 4 + c22 * c ** 4 + ((c11 * c22 - c12 ** 2) / c44 - 2 * c12) * c ** 2 * s ** 2)

poisson_r = -((c11 + c22 - (c11 * c22 - c12 ** 2) / c44) * c ** 2 * s ** 2 - c12 * (s ** 4 + c ** 4)) / (
            c11 * s ** 4 + c22 * c ** 4 + ((c11 * c22 - c12 ** 2) / c44 - 2 * c12) * c ** 2 * s ** 2)
print(str(i)+': '+'min: '+str(poisson_r.min())+' : '+str(poisson_r.max()))
young_module(theta, young_m,title=i+'YM')
poisson_ratio(theta, poisson_r,title=i+'PS')
# elastic=pd.read_excel('C11C12C44.xlsx',index_col=0)
# print(elastic)
# for i in elastic.index:
#     c11=elastic.loc[i][0]
#     c22=c11
#     c12=elastic.loc[i]['C12']
#     c44=elastic.loc[i][2]
#     print(i)
#     print(c11,c22,c12,c44)
#     theta = np.linspace(0, 2 * np.pi, 500)
#     c = np.cos(theta)
#     s = np.sin(theta)
#     young_m = (c11 * c22 - c12 ** 2) / (
#                 c11 * s ** 4 + c22 * c ** 4 + ((c11 * c22 - c12 ** 2) / c44 - 2 * c12) * c ** 2 * s ** 2)
#
#     poisson_r = -((c11 + c22 - (c11 * c22 - c12 ** 2) / c44) * c ** 2 * s ** 2 - c12 * (s ** 4 + c ** 4)) / (
#                 c11 * s ** 4 + c22 * c ** 4 + ((c11 * c22 - c12 ** 2) / c44 - 2 * c12) * c ** 2 * s ** 2)
#     print(str(i)+': '+'min: '+str(poisson_r.min())+' : '+str(poisson_r.max()))
#     young_module(theta, young_m,title=i+'YM')
#     poisson_ratio(theta, poisson_r,title=i+'PS')