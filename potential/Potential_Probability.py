import scipy.constants as sc
import numpy as np
def Tuneling_Pro(phi,w):
    hbar=sc.physical_constants['reduced Planck constant in eV s'][0]
    m_e=sc.physical_constants['electron mass'][0]
    cons1=-2*2**0.5*m_e**0.5/hbar
    e_v=sc.physical_constants['electron volt-joule relationship'][0]
    cons2=e_v**0.5*1.0e-10/e_v
    P_TB=np.exp(cons1*cons2*w*phi**0.5)
    print("P_TB is {}".format(P_TB))
    return P_TB
if __name__=="__main__":
    phi=float(input("Enter Potential Height(eV): "))
    w=float(input("Enter Potential Width(Angstrom): "))
    Tuneling_Pro(phi,w)