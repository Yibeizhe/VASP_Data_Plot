import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Set New Times Roman font for plotting
from matplotlib import rcParams
rcParams['font.family']='serif'
rcParams['font.serif']=['Times New Roman']
e1c2d=pd.read_excel('x_energy.xlsx')
# print(e1c2d.columns)
# print(e1c2d['Strain'])
# plt.plot(e1c2d['Strain'],e1c2d['Energy'])
#plt.plot(e1c2d['Strain']-1,e1c2d['VBM']-e1c2d['Vaccum'])
E1 = np.polyfit(e1c2d['Strain']-1,e1c2d['CBM']-e1c2d['Vaccum'], 1)
e1=np.poly1d(E1)
print(e1)
C2d=np.polyfit(e1c2d['Strain']-1,e1c2d['Energy'], 2)
c2d=np.poly1d(C2d)
print(c2d)
a1=4.0935195692719937
a2=7.0901494424232574
print(2*41.45*1.6*10/(a1*a2))
# plt.plot(e1c2d['Strain']-1,e1c2d['CBM']-e1c2d['Vaccum'])
plt.show()

