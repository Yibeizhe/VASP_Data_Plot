import numpy as np
import re
import pandas as pd

class PoscarDivideElements:
    """
    Created by Junfei Ding 2021/04/07 01:53 Nanjing.NJUST.
    Divide POSCAR/CONTCAR into another POSCAR
    according to the entering elements
    """

    def __init__(self,pos):
        with open(pos) as p:
            self.pos=p.readlines()
        #The six line in poscar is the elements
        self.elements=self.pos[5].split()
        print("The elements are {} in your file".format(self.elements))
        # The seven line in poscar is the number of each element.
        self.elements_num=self.pos[6].split()
        # Find the "Direct" line number.
        for i in range(6,10):
            # Find the line number of "[Dd]irect" in POSCAR
            #This is because, sometimes, "Selective..." is in the POSCAR
            #And usually the line number is between 6 and no more then 10 lines.
            if re.match('^[Dd]',self.pos[i]) is not None:
                self.direct_line = i
        self.select_elements=input("Enter the Elements you want to include in your new POSCAR.\n"
                                   "Note separate them by space: ").split()
        # get a,b,c axis of the lattice,respectively.
        self.axis_a=np.array(self.pos[2].split(),dtype=float)
        self.axis_b = np.array(self.pos[3].split(), dtype=float)
        self.axis_c = np.array(self.pos[4].split(), dtype=float)
        #get the scale rate from the second line
        self.scale_rate=float("".join(self.pos[1].split()))


    def lattice_colume(self):
        #Calculate the volume of the lattice which can be obtained from a*(b cross products c)
        volume=self.scale_rate**3*(self.axis_a[0]*(self.axis_b[1]*self.axis_c[2]-self.axis_b[2]*self.axis_c[1])\
               -self.axis_a[1]*(self.axis_b[0]*self.axis_c[2]-self.axis_b[2]*self.axis_c[0])\
               +self.axis_a[2]*(self.axis_b[0]*self.axis_c[1]-self.axis_b[1]*self.axis_c[0]))
        return volume


    def start_lines(self):
        #Get the starting line number of each element in POSCAR/CONTCAR
        start_line = [0]
        for i in self.elements:
            element_order = self.elements.index(i)
            if element_order != 0:
                elements_pre = 0
                for j in range(element_order):
                    elements_pre += int(self.elements_num[j])
                start_line.append(elements_pre)
        elements_start_num=[i+self.direct_line for i in start_line]
        return elements_start_num


    def end_lines(self):
        elements_end_num=[self.start_lines()[i]+int(self.elements_num[i])
                          for i in range(len(self.elements_num))]
        return elements_end_num


    def pos_pandas(self):
        #Put the elements, elenments number, starting and end line number
        # of the atoms coordinates of each element in to a pandas DataFrame
        ele_index=['Element_number','Start_line','End_line']
        values=np.zeros((len(ele_index),len(self.elements)))
        pos_pd=pd.DataFrame(values,index=ele_index,columns=self.elements)
        pos_pd.loc['Element_number']=self.elements_num
        pos_pd.loc['Start_line'] = self.start_lines()
        pos_pd.loc['End_line'] = self.end_lines()
        return pos_pd


    def select_elements_num(self):
        elements_num_new=list(self.pos_pandas().loc['Element_number'][self.select_elements])
        return elements_num_new


    def write_pos(self):
        pos_name="POSCAR_{}".format("".join(self.select_elements))
        with open(pos_name,'w') as new_poscar:
            #Write the lattice part to patitioned poscar
            print("Write the lattice part")
            for i in range(self.direct_line+1):
                new_poscar.write(self.pos[i])

            for j in self.select_elements:
                print("Write the {} element atoms coordinates to {}".format(j,pos_name))
                j_s=int(self.pos_pandas()[j]['Start_line'])
                j_e=int(self.pos_pandas()[j]['End_line'])
                for k in range(j_s+1,j_e+1):
                    new_poscar.write(self.pos[k])

        lines=open(pos_name,'r').readlines()
        #Change the original elements to your selected elements.
        print("Change the original elements to your selected elements")
        lines[5]="  ".join(self.select_elements)+"\n"
        #Change the corresponding element atoms number.
        print("Change the corresponding element atoms' number.")
        lines[6]="  ".join(self.select_elements_num())+"\n"
        out=open(pos_name,'w')
        out.writelines(lines)
        out.close()

if __name__ == "__main__":
    chos=int(input("Enter 1 to partition POSCAR; 2 CONTCAR:  "))
    if chos==1:
        pos='POSCAR'
    if chos==2:
        pos = 'CONTCAR'
    # pos = 'POSCAR'
    structure=PoscarDivideElements(pos)
    structure.write_pos()
    print(structure.lattice_colume())
