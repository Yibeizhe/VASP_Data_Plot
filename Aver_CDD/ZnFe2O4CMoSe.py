import numpy as np
import matplotlib.pyplot as plt
import os

def averChar(file):
    averC = np.loadtxt(file, comments='#')
    angst=averC[:,0]
    e=averC[:,1]
    return angst,e

print(3**0.5,7**0.5,13**0.5)
print(4.06*13**0.5)
print((4.06*3-3.292946*13**0.5)/3.292946*13**0.5)
print(np.arcsin(1/13**0.5)*180/np.pi)