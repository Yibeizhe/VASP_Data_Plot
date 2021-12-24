import numpy as np
import matplotlib.pyplot as plt
import os

def total_dos(tdos='TDOS.dat'):
    '''Plot total dos including spin or no-spin'''
    with open(tdos,'r') as dos:
        #Decide spin up, spin down or no spin
        dos_name=dos.readlines()[0].split()
    dos_data=np.loadtxt(tdos)
    #Decide how many columns in dos file
    dos_column=dos_data.shape[1]
    energy=dos_data[:,0]
    for i in range(5,10):
        plt.plot(energy,dos_data[:,i],label=dos_name[i])

def partial_dos(dos):
    # Decide how many columns in partial dos file
    colors=['green','seagreen','orange','wheat','red','darkred']
    with open(dos,'r') as f:
        pa_dos_name=f.readlines()[0].split()
    print('Dos include: ',pa_dos_name)
    pa_dos=np.loadtxt(dos)
    pa_dos_column=pa_dos.shape[1]
    energy=pa_dos[:,0]
    for i in range(1,pa_dos_column):
        plt.plot(energy,pa_dos[:,i],color=colors[i-1],label=pa_dos_name[i])

def element_dos(e_dos):
    '''Usually we will use the PDOS_* files to plot the pdos'''
    ele_dos=np.loadtxt(e_dos)
    energy=ele_dos[:,0]
    p_dos=ele_dos[:,-1]
    plt.plot(energy,p_dos,label=e_dos)

def pdos_files():
    pdos_files_name=[]
    pdos_s=os.listdir(os.getcwd())
    for i in pdos_s:
        if 'PDOS' in i:
            pdos_files_name.append(i)
    return pdos_files_name

def file_list():
    # List all the file in current directory
    dos_files=[]
    file_name = os.listdir(os.getcwd())
    choose_string=input('Enter your string to choose your files: ')
    for i in file_name:
        if choose_string in i:
            dos_files.append(i)
    return dos_files

def dos_plot():
    plt.figure(figsize=(3,4),dpi=300)
    # total_dos()
    plt.axhline(y=0,linestyle='--',color='grey',linewidth=0.7)
    plt.axvline(x=0,linestyle='--',color='red')
    plt.legend(fontsize='xx-small')
    # plt.xlim(-2,2)
    # plt.ylim(-2,2)
total_dos('PDOS_Mn_DW.dat')
plt.legend()
plt.show()

