import scipy.constants as sc
import numpy as np
print('The reduced Planck constant in eV s is {}'\
      .format(sc.physical_constants['reduced Planck constant in eV s']))
hbar=sc.physical_constants['reduced Planck constant in eV s'][0]
print('The electron mass is {}'\
      .format(sc.physical_constants['electron mass']))
m_e=sc.physical_constants['electron mass'][0]
cons1=-2*2**0.5*m_e**0.5/hbar
print('Now we have get the first constant {}, and note the unit is sqrt(kg)/(eV*s)'.format(cons1))