import numpy as np

class RotateAxisAB:
    """
        Rotate a and b axes along c axis.
        Namely 3rd and 4th lines in POSCAR, according to the
        rotating angle you input.
        After modification, the content will be written to POSCAR_angle file.
    """
    def __init__(self,pos):
        with open(pos) as p:
            self.pos=p.readlines()
        self.axis_a=np.array(self.pos[2].split(),dtype=float)[0:2]
        self.axis_b = np.array(self.pos[3].split(), dtype=float)[0:2]
        print('a,b axis is: ',self.axis_a,self.axis_b)

    def rotate_theta(self):
        self.theta_d=float(input('Enter the rotating angle (Degree): '))
        theta=np.deg2rad(self.theta_d)
        # The rotating array
        rotate_array=np.array([[np.cos(theta),-np.sin(theta)],
                              [np.sin(theta),np.cos(theta)]],dtype='float')
        print(rotate_array)
        axis_a_rotate=np.dot(rotate_array,self.axis_a)
        axis_b_rotate=np.dot(rotate_array,self.axis_b)
        # print(axis_a_rotate,axis_b_rotate)
        return axis_a_rotate,axis_b_rotate

    def write_ab(self):
        #a,b is the rotated axises which are numpy arrays
        a,b=self.rotate_theta()
        #a axis in POSCAR
        axis_a=self.pos[2].split()
        #turn an array to a list
        axis_a[0:2]=a.tolist()
        axis_a=[str(i) for i in axis_a]
        axis_b=self.pos[3].split()
        axis_b[0:2] = b.tolist()
        axis_b = [str(i) for i in axis_b]
        print('type(axis_a)',type(axis_a),axis_a)
        pos_axis_a="    ".join(axis_a)
        pos_axis_b="    ".join(axis_b)
        self.pos[2]=pos_axis_a+'\n'
        self.pos[3]=pos_axis_b+'\n'
        print(pos_axis_a,pos_axis_b)
        with open('POSCAR_rotate_{}'.format(self.theta_d),'w') as p:
            for line in self.pos:
                p.write(line)
pos=RotateAxisAB('POSCAR')
pos.write_ab()
print(pos.theta_d)