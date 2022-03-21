import os
d=os.getcwd()
print(d)
dirs=os.listdir()
pdos_dir=[]
for i in dirs:
    if os.path.isdir(i) and 'CuIn' in i:
        print(i)
        pdos_dir.append(i)
for dir in pdos_dir:
    print(dir)
    os.chdir(dir)
    print(os.getcwd())
    pdos_elements = []
    pdos=os.listdir()
    for elements in pdos:
        ele=elements.split('_')[1].split('.')[0]
        pdos_elements.append(ele)
    print(pdos_elements)
    print(pdos)
    os.chdir('..')
    print(os.getcwd())

