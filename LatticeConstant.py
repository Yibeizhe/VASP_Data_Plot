metal={'Al':4.039,'Ag':4.161,'Au':4.171,
       'Pt':3.977,'Mg':4.506,'Cu':3.621,
       'Ni':3.506,'Pd':3.957,'Co':3.520,'Cr':3.624}
CrX3={'CrI3':7.089,'CrBr3':6.438,'CrCl3':6.056}
Xene={'Graphene':2.469}
MoX2={'MoS2':3.190}
# Metal(111) lattice
for k in metal:
    print(k+'(111)','=',metal[k]*2**0.5*0.5*2)
# print(2.469*2**0.5*2)
# for j in range(10):
#     print(j,Xene['Graphene']*j**0.5)
# print((6.53-6.38)/6.38)

