import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import rcParams
from matplotlib.pyplot import MultipleLocator
# from matplotlib.font_manager import FontProperties
# Set times New Times Roman
# plt.rcParams.update({'font.size': 5})
plt.rc('legend', fontsize=7)
rcParams['font.family']='serif'
rcParams['font.serif']=['Times New Roman']
rcParams['axes.linewidth'] =1
class ElementDos():
    def __init__(self,dos):
        # Get the dos name namel  s p dx dxy...
        with open(dos,'r') as dosfile:
            self.dos_name=dosfile.readlines()[0].split()
        self.dos_data=np.loadtxt(dos)
        # Energy
        self.energy=self.dos_data[:,0]
        # Decide how many columns in dos file
        self.dos_columns = self.dos_data.shape[1]
        # Energy maximum
        self.me=self.energy.max()
        # Energy minimum
        self.ne=self.energy.min()
        # put the dos file in pandas DataFrame
        self.dos_frame=pd.DataFrame(self.dos_data,columns=self.dos_name)
        #Difine the plotting color


    # tot plot
    def tot_plot(self,label='tot',color='grey'):
        plt.plot(self.energy,self.dos_frame['tot'],
                 label=label,color=color,linewidth='0.5')


elements=input("Enter elements' name separated by space: ").split()
print(elements)
elements_pdos=[]
for i in elements:
    j='PDOS_'+i+'.dat'
    elements_pdos.append(j)
print(elements_pdos)

fig = plt.figure(figsize=(4,3), dpi=300)
colors = ['blue', 'orange', 'green', 'red', 'purple',
          'brown', 'pink', 'grey', 'olive', 'cyan']
for i in range(len(elements)):
    ElementDos(elements_pdos[i]).tot_plot(label=elements[i],color=colors[i])
plt.xlim(-2,2)
plt.legend()
plt.show()