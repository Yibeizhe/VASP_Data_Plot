import numpy as np
with open('CHGCAR') as chgcar:
    file=chgcar.readlines()
    print(file[5])
    atom_class=file[5].split()

    #The 7th line is the number of each elements,
    #We need to sum  up all of these numbers to get
    # how many lines in CHGCAR are the atoms coordinates.
    atom_class_num=sum(np.array(file[6].split(),dtype='int'))

    #Find the FFT grid number
    charge_fft_line=8+atom_class_num+1
    charge_fft=np.array(file[charge_fft_line].split(),dtype=int)

    print(charge_fft)
#multiply all elements in a numpy array
fft_grids=np.prod(charge_fft)
print(fft_grids)
#get the charge density part in CHGCAR file.

with open('CHGCAR') as chgcar:
    file=chgcar.readlines()
    with open('chg.dat','w+') as chg:
        for i in range(charge_fft_line+1,charge_fft_line+1+int(fft_grids/5)):
            chg.write(file[i])
chgc=np.genfromtxt('chg.dat')
dd=chgc.reshape(80,80,80)
print(dd.sum(axis=(0,1)))