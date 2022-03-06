import matplotlib.pyplot as plt
import numpy as np
aver=np.loadtxt('PLANAR_AVERAGE.dat',comments='#')
plt.figure(figsize=(4,3))
plt.plot(aver[:,0],aver[:,1])
plt.show()