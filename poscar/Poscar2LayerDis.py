import os


# Read how many lines in poscar
def len_pos(file):
    with open(file, 'r') as pos:
        length = len(pos.readlines())
    return length


# Get the position part of poscar
def readps(poscar):
    '''In this function we will get
    1 how many lines in poscar;
    2 how many atoms in poscar;
    3 return the atoms coordinates in a list'''
    pos = []  # Define a list and then put the position part of poscar in this list.
    pos1 = 1  # Calculate how many lines which is not the atoms coordinates there are in pocar.

    with open(poscar, 'r') as tr:
        line = tr.readline()
        while line != '':  # use while loop to read the non-atomic coordinates part in poscar,do nothing else except this
            pos1 += 1
            line = tr.readline()
            if 'Direct' in line:
                break  # finish to read the non-atom coordinates part.
        print('\nThere are {} lines in non-coordinates parts\n'.format(pos1))

        lens = len_pos(poscar)  # Count how mant lines in poscar
        print('There are {} lines in poscar.\n'.format(lens))

        atoms = lens - pos1
        print('There are {} atoms in poscar.\n'.format(atoms))
        for i in range(atoms):
            line = tr.readline()
            with open('position', 'w') as posi:
                posi.write(line)
                pos.append(line)
        return pos


# get a,b and c direction coordinates, respectively.
def abc_coordinate(atoms):
    atoms_abc = []
    # axis=float(input("In which axis you want to calculate the average distance? \n a axis press 0, \n b 1 \n c 2 \n\n"))
    axis = 2
    for i in range(len(atoms)):
        if axis == 0:
            atoms_abc.append(atoms[i].split()[0])
        elif axis == 1:
            atoms_abc.append(atoms[i].split()[1])
        elif axis == 2:
            atoms_abc.append(atoms[i].split()[2])
        else:
            print('Invalid input!')
    return atoms_abc


# get all the elements which meet certain conditions in the list.
def range_list(a, lower_li, upper_li):
    range_atoms = []
    lower_limit = float(lower_li)
    upper_limit = float(upper_li)
    for i in range(len(a)):
        if lower_limit <= float(a[i]) <= upper_limit:
            range_atoms.append(a[i])
    # print(range_l)
    return range_atoms


# average all the elements in the list.
def aver_list(a):
    sumlist = 0
    for i in range(len(a)):
        sumlist += float(a[i])
    return sumlist / len(a)


# average distance between two layers
file = str(input('Enter your file name:\n'))
atoms_cor = readps(file)
atom_abc = abc_coordinate(atoms_cor)

atom_range1 = range_list(atom_abc, 0.45, 0.50)
print('\n The following is the choosed atom a,b or c coordinate in first layer')
print(atom_range1)
atom_aver1 = aver_list(atom_range1)
print('There are {} atoms choosed'.format(len(atom_range1)))
print('Average coordinates of the first layer is:')
print(atom_aver1, '\n')

atom_range2 = range_list(atom_abc, 0.58, 0.61)
print('The following is the choosed atom a,b or c coordinate  in second layer')
print(atom_range2)
atom_aver2 = aver_list(atom_range2)
print('There are {} atoms choosed'.format(len(atom_range2)))
print('Average coordinates of the second layer is:')
print(atom_aver2, '\n')

aver_dis = abs(float(atom_aver1) - float(atom_aver2))
print('Average coordinates distance is:')
print(aver_dis, '\n')

lattice_aver_dis = 60.0 * aver_dis
print('Average two layer distance in {} is:'.format(file))
print(lattice_aver_dis)