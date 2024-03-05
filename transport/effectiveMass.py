import numpy as np
# read the a,b and c axis values from the POSCAR files.
with open('POSCAR','r') as poscar:
    pos=poscar.readlines()
axis_a = np.array(pos[2].split()[0:3], dtype=float)
axis_b = np.array(pos[3].split()[0:3], dtype=float)
axis_c = np.array(pos[4].split()[0:3], dtype=float)
print(axis_a,axis_b,axis_c)

# convert the unit from angstrom to Bohr
axis_a=axis_a/0.5292
axis_b=axis_a/0.5292
