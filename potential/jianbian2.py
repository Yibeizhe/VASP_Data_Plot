import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch

xx=np.arange(-2*np.pi,2*np.pi,0.01)
yy=np.sin(xx)

path = Path(np.array([xx,yy]).transpose())
patch = PathPatch(path, facecolor='none')
plt.gca().add_patch(patch)

im = plt.imshow(xx.reshape(yy.size,1),  cmap=plt.cm.Blues,interpolation="bicubic",
                origin='lower',extent=[-2*np.pi,2*np.pi,-1,1],aspect="auto",clip_path=patch, clip_on=True)
im.set_clip_path(patch)
plt.show()