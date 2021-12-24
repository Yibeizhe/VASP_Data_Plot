metal={'Al':4.03893,'Ag' :4.160549,'Au':4.171289,'Pt': 3.976771,
       'Mg':4.5056,'Cu':3.621,'Ni':3.506, 'Pd':3.957,
       'Co':3.520,'Cr': 3.624}
CrX3={'CrI3':6.93258,'CrBr':6.38909,'CrCl3':5.97958,'In2Se3':4.10712}

for k in metal:
    print(k + '(111)', ' = ',metal[k]*2**0.5*0.5)
for k in metal:
    print('sqrt(5)'+k + '(111)', ' = ', metal[k]*2**0.5*0.5*5**0.5)
for k in metal:
    print('sqrt(3)'+k + '(111)', ' = ', metal[k]*2**0.5*0.5*3**0.5)