import numpy as np
# import matplotlib.pyplot as plt
# Created By Junfei Ding At NJUST 2022/10/25
def reci_lattice_array():
    with open('POSCAR','r') as pos:
        p=pos.readlines()
    #Transform anstrom to bohr
    a = np.array(p[2].split(), dtype=float)/0.5292
    b = np.array(p[3].split(), dtype=float)/0.5292
    c = np.array(p[4].split(), dtype=float)/0.5292
    # Abtain the volume of lattice in (1/bohr)**3
    volume=np.dot(np.cross(a,b),c)
    # Abtain the reciprocal lattice vector b1,b2,b3
    b1=2*np.pi / volume*np.cross(b,c)
    b2 = 2 * np.pi / volume * np.cross(c, a)
    b3 = 2 * np.pi / volume * np.cross(a, b)
    # Abtain the transform matrix of reciprocal space
    b_array=np.stack((b1,b2,b3))
    print("The transform matrix of reciprocal space is : ")
    print(b_array)
    return b_array

def k_points():
    """
    Obtain the k points along the band line.
    """
    with open('KPOINTS','r') as kps:
        ks=kps.readlines()
    # k points number between two high-symmetry points
    kn=int(ks[1])
    b_array=reci_lattice_array()
    # Transform matrix
    k1=np.array(ks[4].split()[0:3],dtype='float')
    # Transform k1 point from in direct space to in reciprocal space
    # multiplied by the transform matrix
    k1b=k1@b_array
    k2 = np.array(ks[5].split()[0:3], dtype='float')
    k2b = k2 @ b_array
    k3= np.array(ks[8].split()[0:3], dtype='float')
    k3b = k3 @ b_array
    # Obtain the distance between two k points
    dk21b=np.linalg.norm(k2b-k1b)
    dk23b = np.linalg.norm(k3b - k2b)
    # Since the k path is a rectangle, the two sides' length of the
    # rectangle are dk21b and dk23b respectively,
    # accordingly, we can calculate the k points along the band line.
    kd=[0,dk21b,dk21b+dk23b,2*dk21b+dk23b,2*(dk21b+dk23b)]
    ks=[]
    for i in range(len(kd) - 1):
        step_i = (kd[i + 1] - kd[i]) / (kn - 1)
        for j in range(kn):
            ks.append(kd[i] + j * step_i)
    return kn,ks

def vbm_cbm():
    with open("BAND_GAP",'r') as f:
        bd=f.readlines()
    spin=int(input("Spin band? Enter 1. Otherwise No spin: "))
    if spin==1:
        for i in bd:
            if "Lowest" in i:
                print(i)
                band_cbm=i.split(':')[1].split()
                bc_up_n=int(band_cbm[0])
                bc_dw_n=int(band_cbm[1])
                bc_t_n=int(band_cbm[-1])
                # print(bc_up_n,bc_dw_n,bc_t_n)
            elif "Highest" in i:
                print(i)
                band_vbm=i.split(':')[1].split()
                bv_up_n=int(band_vbm[0])
                bv_dw_n=int(band_vbm[1])
                bv_t_n=int(band_vbm[-1])
                # print(bv_up_n,bv_dw_n,bv_t_n)
        return bc_up_n,bc_dw_n,bv_up_n,bv_dw_n,bv_t_n,bc_t_n
    else:
        for i in bd:
            if "HOMO" in i:
                print(i)
                band_vc_n=i.split(":")[1].split()
                bv_t_n=band_vc_n[0]
                bc_t_n=band_vc_n[1]
        return bv_t_n,bc_t_n

def band():
    with open('BAND.dat','r') as b:
        bd=b.readlines()
    kps_n=int(bd[1].split(":")[1].split()[0])
    band_n=vbm_cbm()
    band_vbm_n=int(band_n[-2])
    band_cbm_n = int(band_n[-1])
    with open('Band_vbm.dat','w') as vbm:
        for i in range(2+(band_vbm_n-1)*(kps_n+2),band_vbm_n*(kps_n+2)+1):
            vbm.write(bd[i])
            # print(bd[i])
    vbm_array=np.loadtxt('Band_vbm.dat',comments='#',dtype='float')
    # For the even band, the data along the k points are reverse
    if band_vbm_n % 2==0:
        # if vbm_array.shape[1]==3, band is for spin
        if vbm_array.shape[1]==3:
            vbm_array[:, 0] = vbm_array[:, 0][::-1]
            vbm_array[:, 1] = vbm_array[:, 1][::-1]
            vbm_array[:, 2] = vbm_array[:, 2][::-1]
        else:
            vbm_array[:, 0] = vbm_array[:, 0][::-1]
            vbm_array[:, 1]=vbm_array[:,1][::-1]
    with open('Band_cbm.dat','w') as cbm:
        for j in range(2+(band_cbm_n-1)*(kps_n+2),band_cbm_n*(kps_n+2)+1):
            cbm.write(bd[j])
            # print(bd[j])
    cbm_array=np.loadtxt('Band_cbm.dat',comments='#',dtype='float')
    if band_cbm_n % 2==0:
        # if vbm_array.shape[1]==3, band is for spin
        if cbm_array.shape[1]==3:
            cbm_array[:, 0] = cbm_array[:, 0][::-1]
            cbm_array[:, 1] = cbm_array[:, 1][::-1]
            cbm_array[:, 2] = cbm_array[:, 2][::-1]
        else:
            cbm_array[:, 0] = cbm_array[:, 0][::-1]
            cbm_array[:, 1]=cbm_array[:,1][::-1]
    return vbm_array, cbm_array

def mstar():
    fit_ps=int(input("Enter the number of points used as fitting,such as 6 or 8: "))
    k=k_points()
    kn=int(k[0])
    ks=k[1]
    #The first segment of K points
    k_fits_1=ks[kn - fit_ps:kn]
    # The second segment of K points
    k_fits_2=ks[kn:kn + fit_ps]
    # Obtain the band data containing the VBM and CBM.
    vbm_cbm=band()
    # The first element of vbm_cbm is vbm band
    vbm_band=vbm_cbm[0]
    # The second element of vbm_cbm is cbm band
    cbm_band=vbm_cbm[1]
    # Two segments of vbm band used as to fit the mass
    vbm_band_en_t_1=vbm_band[:,-1][kn-fit_ps:kn]
    vbm_band_en_t_2 = vbm_band[:, -1][kn:kn+fit_ps]
    # Two segments of cbm band used as to fit the mass
    cbm_band_en_t_1=cbm_band[:,-1][kn-fit_ps:kn]
    cbm_band_en_t_2 = cbm_band[:, -1][kn:kn+fit_ps]

    print(5*"*"+"Fitting the efficient mass of VBM 1"+5*"*")
    m_vbm_1 = np.polyfit(k_fits_1, vbm_band_en_t_1/27.12, 2)
    m_vbm1 = np.poly1d(m_vbm_1)
    print(m_vbm1)
    print("Efficient mass of VBM 1 is: {}".format(1/(2*m_vbm_1[0])))

    print(5*"*"+"Fitting the efficient mass of VBM 2"+5*"*")
    m_vbm_2 = np.polyfit(k_fits_2, vbm_band_en_t_2/27.12, 2)
    m_vbm2=np.poly1d(m_vbm_2)
    print(m_vbm2)
    print("Efficient mass of VBM 2 is: {} ".format(1/(2*m_vbm_2[0])))

    print(5*"*"+"Fitting the efficient mass of CBM 1"+5*"*")
    m_cbm_1 = np.polyfit(k_fits_1, cbm_band_en_t_1/27.12, 2)
    m_cbm1=np.poly1d(m_cbm_1)
    print(m_cbm1)
    print("Efficient mass of CBM 1 is: {}".format(1/(2*m_cbm_1[0])))

    print(5*"*"+"Fitting the efficient mass of CBM 2"+5*"*")
    m_cbm_2 = np.polyfit(k_fits_2, cbm_band_en_t_2/27.12, 2)
    m_cbm2 = np.poly1d(m_cbm_2)
    print(m_cbm2)
    print("Efficient mass of CBM 1 is: {} ".format(1/(2*m_cbm_2[0])))

if __name__=="__main__":
    mstar()


