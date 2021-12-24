import sys
sys.path.append('..')
from  CrBr3_CH import DosPlot as dp
import matplotlib.pyplot as plt
crp=dp('PDOS_Br_DW.dat')
plt.plot(crp.energy,crp.dos_frame['tot'])
plt.plot(crp.energy,crp.pdos())
plt.show()
