import numpy as np
import re
import pandas as pd
class Poscar_TF:
    def __init__(self, pos):
        with open(pos) as p:
            self.pos = p.readlines()
        # The six line in poscar is the elements
        self.elements = self.pos[5].split()
        print("The elements are {} in your file".format(self.elements))
        # The seven line in poscar is the number of each element.
        self.elements_num = sum(int(i) for i in self.pos[6].split())
        print(f'There are {self.elements_num} atoms in file.')
        # Find the "Direct" line number.
        for i in range(6, 10):
            # Find the line number of "[Dd]irect" in POSCAR
            # This is because, sometimes, "Selective..." is in the POSCAR
            # And usually the line number is between 6 and no more then 10 lines.
            if re.match('^[Dd]', self.pos[i]) is not None:
                self.direct_line = i
        print(f'The D/direct line number is {self.direct_line}')

    def poscar_tf(self,condition_tf):
        # Write the lattice part to modified poscar
        with open('POSCAR_TF','w') as poscar:
            for i in range(self.direct_line):
                poscar.write(self.pos[i])
            # Write "Selective dynamics" line to POSCAR
            poscar.write('Selective dynamics\n')
            # Write the "Direct line" to the POSCAR
            poscar.write(self.pos[self.direct_line])
            for j in range(self.direct_line+1,self.direct_line+self.elements_num+1):
                if float(self.pos[j].split()[2])<condition_tf:
                    self.pos[j]=self.pos[j].replace('\n','')+" F F F\n"
                else:
                    self.pos[j] = self.pos[j].replace('\n','')+" T T T\n"
                poscar.write(self.pos[j])

if __name__=='__main__':
    pos=Poscar_TF('POSCAR')
    pos.poscar_tf(0.5)




