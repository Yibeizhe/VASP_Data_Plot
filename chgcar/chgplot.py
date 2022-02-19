import numpy as np
import matplotlib.pyplot as plt
plt.rc('font',family='Times New Roman')
chg=np.loadtxt('chg11.dat',comments='#')
plt.plot(chg[:,0],chg[:,1])
plt.show()