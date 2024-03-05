#！
class Eigenval():
    def __init__(self,eigenval):
        with open(eigenval,'r') as eigen:
            self.eigen=eigen.readlines()

            # The 1st number in 6th line of EIGNVAL file is the number of electrons
            self.electron = self.eigen[5].split()[0]
            print('There are {} electrons'.format(self.electron))

            # The 2nd number in 6th line of EIGNVAL file is the number of bands
            self.ks=int(self.eigen[5].split()[1])
            print('There are {} k points'.format(self.ks))

            # The 3rd number in 6th line of EIGNVAL file is the number of bands
            self.nbands = int(self.eigen[5].split()[2])
            print('There are {} bands'.format(self.nbands))

    def ei_up(self):
        with open("EIGENVAL_UP", 'w') as ei_u:
            for i in range(6):
                print(self.eigen[i])
                ei_u.write(self.eigen[i])
            for band in range(6,self.nbands+6+2):
                if band == 6:
                    ei_u.write(self.eigen[band])
                elif band == 7 :
                    ei_u.write(self.eigen[band])
                else:
                    l=self.eigen[band].split()
                    l.pop(2)
                    l.pop(3)
                    print(l)
                    ei_u.write(' '.join(l) + '\n')

            for k in range(1,self.ks):
                for band in range((k*(self.nbands+2)+6),((k+1)*(self.nbands+2)+6)):
                    if band==6+k*(self.nbands+2):
                        ei_u.write(self.eigen[band])
                    elif band ==7  + k * (self.nbands + 2):
                        ei_u.write(self.eigen[band])
                    else:
                        l = self.eigen[band].split()
                        l.pop(2)
                        l.pop(3)
                        print(l)
                        ei_u.write(' '.join(l) + '\n')

    def ei_dw(self):
        with open("EIGENVAL_DW", 'w') as ei_u:
            for i in range(6):
                print(self.eigen[i])
                ei_u.write(self.eigen[i])
            for band in range(6, self.nbands + 6 + 2):
                if band == 6:
                    ei_u.write(self.eigen[band])
                elif band == 7:
                    ei_u.write(self.eigen[band])
                else:
                    l = self.eigen[band].split()
                    l.pop(1)
                    l.pop(2)
                    print(l)
                    ei_u.write(' '.join(l) + '\n')

            for k in range(1, self.ks):
                for band in range((k * (self.nbands + 2) + 6), ((k + 1) * (self.nbands + 2) + 6)):
                    if band == 6 + k * (self.nbands + 2):
                        ei_u.write(self.eigen[band])
                    elif band == 7 + k * (self.nbands + 2):
                        ei_u.write(self.eigen[band])
                    else:
                        l = self.eigen[band].split()
                        l.pop(1)
                        l.pop(2)
                        print(l)
                        ei_u.write(' '.join(l) + '\n')
t=Eigenval("EIGENVAL")
t.ei_up()
t.ei_dw()
