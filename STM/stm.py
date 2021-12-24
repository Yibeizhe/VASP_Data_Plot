
import numpy as np
import matplotlib as mpl
#mpl.use('Agg') #silent mode
from matplotlib import pyplot as plt

x_mesh=np.loadtxt('X.grd')
y_mesh=np.loadtxt('Y.grd')
v_mesh=np.loadtxt('STM_0.40.grd')

fig = plt.figure()
cmap = plt.cm.get_cmap("Greys_r")
plt.contourf(x_mesh,y_mesh,v_mesh,cmap=cmap)

plt.axis('equal')
plt.axis('off')

plt.savefig("STM.jpg",dpi=300)
plt.show()