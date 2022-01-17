#Created by Junfei Ding 2021/07/30 20:46 Nanjing.NJUST.
import re
import numpy as np
class PoscarDivideElements():
    """
    Calculate the average distance of two layers in poscar
    according to the entering coordinates of each layer
    """
    def __init__(self,pos):
        with open(pos) as p:
            self.pos=p.readlines()
        for i in range(6,10):
            # Find the line number of "[Dd]irect" in POSCAR
            #This is because, sometimes, "Selective..." is in the POSCAR
            #And usually the line number is between 6 and no more then 10 lines.
            if re.match('^[Dd]',self.pos[i]) is not None:
                self.direct_line = i

        # Get each the number of each elements from 7th line
        self.elements_num=self.pos[6].split()
        # Get how many atoms in poscar
        self.elements_num_sum=sum(int(i) for i in self.elements_num)
        print('There are {} atoms in poscar.'.format(self.elements_num_sum))
        # C direction lattice constant
        self.c_lattice_constant = float(self.pos[4].split()[-1])
        print('C lattice constant is {}'.format(self.c_lattice_constant))

    def atom_pos(self):
        '''
        Put all the coordinates of atoms in a array.
        This can be achieved by read all the lines that between the "Direct"
        line and this line plus the total number of atoms line.
        '''
        pos_list=[]
        for i in range(self.direct_line+1,self.direct_line+1+self.elements_num_sum):
            pos_list.append(self.pos[i].split()[0:3])
        pos_array=np.array(pos_list,dtype='float')
        return pos_array

    def selec_pos(self):
        pos_selec=np.copy(self.atom_pos()[:,2])
        a_botom=float(input('Enter the lower limit of atomic coordinates: '))
        pos_botom=pos_selec[pos_selec>a_botom]
        # print('The atomic coordinates  which are larger than lower limit is as following:')
        # print(pos_botom)
        a_upper = float(input('Enter the upper limit of atomic coordinates: '))
        pos_top=pos_botom[pos_botom<a_upper]
        print('The atomic coordinates  which are between the {} and {} limit are as following:'\
              .format(a_botom,a_upper))
        print(pos_top)
        selec_atoms_aver = np.average(pos_top)
        print('The average value of the selected c direction coordinates are :')
        print(selec_atoms_aver)
        select_atoms_c_aver=self.c_lattice_constant*selec_atoms_aver
        print('And its average c lattice is {}.'.format(select_atoms_c_aver))
        return select_atoms_c_aver

    def average2layer(self):
        print('Calculate the average c coordinates of the first layer...')
        c1=self.selec_pos()
        print('Calculate the average c coordinates of the second layer...')
        c2 = self.selec_pos()
        print('The average distance of c direction of these two layer is :')
        c2_c1 = abs(c2 - c1)
        c2c1="{:.3f}".format(c2_c1)
        print(c2c1)


if __name__=="__main__":
    dis=PoscarDivideElements('CONTCAR')
    dis.average2layer()
