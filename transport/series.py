kpoints=[0,0.235041644,0.642145712,0.877186876,1.284290945]
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