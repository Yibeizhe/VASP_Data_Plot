import matplotlib.pyplot as plt
import numpy as np
# https://www.brothereye.cn/python/427/
# https://matplotlib.org/stable/tutorials/colors/colormap-manipulation.html
from matplotlib import cm
CrBr_Eex=np.array([38.98,39.55,39.88,40.26,46.68,47.89,47.82])
CrBr3_Eex=[i-CrBr_Eex[0] for i in CrBr_Eex]
CrBr_name=['$CrBr_3$','$Ben@(Cr_2Br_6)_4$','$Naph@(Cr_2Br_6)_4$',
           '$Azul@(Cr_2Br_6)_4$','$Gr@CrBr_3$','$Gr@CrBr_3-GBs-1$','$Gr@CrBr_3-GBs-2$']
CrBr3_name=['$CrBr_3$','Ben@Br','Naph@Br',
           'Azul@Br','Gr@Br','GBs-1@Br','GBs-2@Br']
for x,y in zip(range(len(CrBr3_Eex)),CrBr3_Eex):
    print(x,y)
norm = plt.Normalize(CrBr_Eex.min(), CrBr_Eex.max())
norm_y = norm(CrBr_Eex)
map_vir = cm.get_cmap(name='Blues')
# color = map_vir(norm_y)
cc="'azure','lightcyan',"
color=['paleturquoise','skyblue','mediumturquoise',
       'aquamarine','turquoise','springgreen','deepskyblue']
wid=0.5
fig, ax = plt.subplots()
# plt.bar(CrBr3_name,CrBr_Eex,color=color,width=wid)
a = np.array([[1, 1],
              [2, 2]])

for x,y in zip(range(len(CrBr3_Eex)),CrBr_Eex):
    ax.imshow(a, interpolation='bicubic', extent=(x, x + wid, 0, y), cmap=plt.cm.Blues_r)
plt.ylim(30,50)
plt.ylabel('Energy(meV)')
plt.xticks(rotation=30)
ax.set_aspect('auto')
plt.show()