import numpy as np
# reciprocal lattice in 1/bohr
b_bohr=np.array([[0.583324361,   0.000000000,   0.000000000],
   [0.000000000,   1.010361793,   0.000000000],
   [0.000000000,   0.000000000,   0.166245924]],dtype='float')
# high symmetry points
k_y=np.array([0.0000000000,   0.5000000000,   0.0000000000],dtype='float')
k_g=np.array([0.0000,      0.3354,      0.0000],dtype='float')
k_x=np.array([0.5000000000,   0.3354,   0.0000000000 ],dtype='float')
k_s=np.array([0.5000000000,   0.5000000000,   0.0000000000 ],dtype='float')

# transfer the symmetry points from fracture lattice to cardi lattice
k_y_c=np.dot(k_y,b_bohr)
k_g_c=np.dot(k_g,b_bohr)
k_x_c=np.dot(k_x,b_bohr)
k_s_c=np.dot(k_s,b_bohr)

# distance between two vector
gy=np.linalg.norm(k_g_c - k_y_c)
xg=np.linalg.norm(k_x_c - k_g_c)
sx=np.linalg.norm(k_s_c - k_x_c)
ys=np.linalg.norm(k_y_c - k_s_c)
print('gy,xg,sx,ys',gy,xg,sx,ys)
k_line=[gy,xg,sx,ys]
kpoints=[0,0,0,0]
kpoints[0]=k_line[0]
for i in range(1,len(k_line)):
   kpoints[i]=kpoints[i-1]+k_line[i]
kpoints.insert(0,0)
print(kpoints)

n=80
ks=[]
for i in range(len(kpoints)-1):
    step_i=(kpoints[i+1]-kpoints[i])/(n-1)
    print(step_i)
    for j in range(n):
        ks.append(kpoints[i]+j*step_i)
print(ks)

with open('ks.dat', 'w') as f1:
    ks=[str(line)+"\n" for line in ks]
    f1.writelines(ks)