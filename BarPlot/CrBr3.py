import matplotlib.pyplot as plt
import numpy as np
# plt.style.use('seaborn-deep')
styles='ggplot'
plt.style.use(styles)
plt.rc('font',family='Times New Roman')
print(plt.style.available)
CrBr_Eex=np.array([38.98,39.55,39.88,40.26,46.68,47.89,47.82])
CrBr3_name=['CrBr$_3$','Ben@Br','Naph@Br',
           'Azul@Br','Gr@Br','GBs-1@Br','GBs-2@Br']
CrX_Energy=np.array([23.67,23.99,24.18,24.39,52.89,57.02,57.23,58.28])
CrX_Name=['CrCl$_3$','Ben@Cl','Naph@Cl','Azul@Cl','CrI$_3$','Ben@I','Naph@I','Azul@I']

# x=np.arange(len(CrBr_Eex))
x=np.arange(len(CrX_Energy))
fig = plt.figure(figsize=(4, 3), dpi=300)

ax=plt.gca()
wid=0.5
# colors=['#00BFC4','#00BFC4','#00BFC4','#F58A78','#00BFC4','#F58A78','#00BFC4']
colors=['#39A1FF','#39A1FF','#39A1FF','#F58A78','#4EC973','#4EC973','#4EC973','#F58A78']
plt.bar(x,CrX_Energy,width=wid,tick_label=CrX_Name,color=colors,label='Cl-E$_{ex}$')
plt.bar(7,12,width=wid,color='#4EC973',label='I-E$_{ex}$')
for x,y in zip(x,CrX_Energy):
    plt.text(x,y+0.1,'{}'.format(y),ha='center',va='bottom',fontsize=8)
# a = np.array([[1, 1],
#               [2, 2]])
#
# for x,y in zip(range(len(CrBr_Eex)),CrBr_Eex):
#     ax.imshow(a, interpolation='bicubic', extent=(x, x + wid, 0, y), cmap=plt.cm.Blues_r)
# ax.set_aspect('auto')
plt.ylim(20,62)
# plt.xticks(rotation=30)
plt.tick_params(axis='both', labelsize=6)
plt.legend(loc=2,fontsize=6,framealpha=0.5)
plt.ylabel('Energy(meV)')
plt.savefig('CrX3',bbox_inches='tight')
plt.show()