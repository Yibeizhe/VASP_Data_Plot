import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

def PDE():
    #时间 s 距离um
    h=2; N=50  # h*N = 100um,
    s=0.0001 ; M=6000  #   s*M= 30s

    c_eq = 34.2;
    hc_eq = 500
    co_eq = 0.7686;
    oh_eq = 0.00033

    dc = 1.91*10**3 ; dhc = 9.23*10**2
    dco = 1.19*10**3 ; doh = 5.27*10**3
    '''
        K1: co2+oh- == hco3-
        k2: hco3+oh == co3 + h2o
    '''
    k1f = 5.93; k1r =k1f/hc_eq*c_eq*oh_eq #1.3386 * 10 ** -4
    k2f = 10**5 ; k2r = k2f/co_eq*hc_eq*oh_eq #2.147766323 * 10 ** 4

    sc = s*dc/h**2 ; shc = s*dhc/h**2
    sco = s*dco/h**2 ; soh = s*doh/h**2

    c_consumption = (50/96485)*(0.25/8+0.1/2+0.05/2+0.4/12)*1000000  # j(c/m2s)/F(c/mol) 与 D(um2/s)*δC/δx（mmol/dm3/um）量纲统一后应乘以10^6
    oh_formation = (50/96485)*(0.1/2+0.1/2+0.25+0.2)*1000000

    #建立网格
    uc=np.zeros([N+1,M+1])
    uhc=np.zeros([N+1,M+1])
    uco=np.zeros([N+1,M+1])
    uoh=np.zeros([N+1,M+1])

    #初始化
    for i in range(0,N+1):
        uc[i,0]=c_eq
        uhc[i,0]=hc_eq
        uco[i,0]=co_eq
        uoh[i,0]=oh_eq
    for j in range(0,M+1):
        uc[0,j] = c_eq
        uhc[0,j] = hc_eq
        uco[0,j] = co_eq
        uoh[0,j] = oh_eq
    #PDE离散化
    for j in range(0,M):
        for i in range(1,N):
            '''uc[i,j+1] = sc*uc[i+1,j]+(1-2*sc)*uc[i,j]+sc*uc[i-1,j]+s*(uhc[i,j]*k1r-uc[i,j]*uoh[i,j]*k1f)
            uhc[i,j+1] = shc*uhc[i+1,j]+(1-2*shc)*uhc[i,j]+shc*uhc[i-1,j]+s*(uc[i,j]*uoh[i,j]*k1f-uhc[i,j]*k1r-uhc[i,j]*uoh[i,j]*k2f+uco[i,j]*k2r)
            uco[i,j+1] = sco*uco[i+1,j]+(1-2*sco)*uco[i,j]+sco*uco[i-1,j]+s*(uhc[i,j]*uoh[i,j]*k2f-uco[i,j]*k2r)
            uoh[i,j+1] = soh*uoh[i+1,j]+(1-2*soh)*uoh[i,j]+soh*uoh[i-1,j]+s*(uhc[i,j]*k1r-uc[i,j]*uoh[i,j]*k1f+uco[i,j]*k2r-uhc[i,j]*uoh[i,j]*k2f)
            '''
            uc[i,j+1] = sc*uc[i+1,j]+(1-2*sc)*uc[i,j]+sc*uc[i-1,j]+s*(uhc[i,j]*k1r-uc[i,j]*uoh[i,j]*k1f)
            uhc[i,j+1] = shc*uhc[i+1,j]+(1-2*shc)*uhc[i,j]+shc*uhc[i-1,j]+s*(uc[i,j]*uoh[i,j]*k1f-uhc[i,j]*k1r-uhc[i,j]*uoh[i,j]*k2f+uco[i,j]*k2r)
            uco[i,j+1] = sco*uco[i+1,j]+(1-2*sco)*uco[i,j]+sco*uco[i-1,j]+s*(uhc[i,j]*uoh[i,j]*k2f-uco[i,j]*k2r)
            uoh[i,j+1] = soh*uoh[i+1,j]+(1-2*soh)*uoh[i,j]+soh*uoh[i-1,j]+s*(uhc[i,j]*k1r-uc[i,j]*uoh[i,j]*k1f+uco[i,j]*k2r-uhc[i,j]*uoh[i,j]*k2f)
            #if uc[i,j+1]<0:
                #uc[i,j+1] = 0.000
                #continue

        #电极边界
        uc[N,j+1] = uc[N-1,j+1]-0.038*h  #  consu/dc = -0.03787131638706104 ~=0.038
        uhc[N,j+1] = uhc[N-1,j+1]
        uco[N,j+1] = uco[N-1,j+1]
        uoh[N,j+1] = uoh[N-1,j+1]+ 0.054*h    # oh_formation/doh = 0.0540831872185892~= 0.054
    #print(sc,sc*uc[2,1]+(1-2*sc)*uc[1,1]+sc*uc[0,1],s*(uhc[1,1]*k1r-uc[1,1]*uoh[1,1]*k1f),' --- ',uc[1,1],uhc[1,1],uoh[1,1])
    i2=N-1
    j2=2
    #print(uc[i2+1,j2],uc[i2,j2],uc[i2-1,j2],sc*uc[i2+1,j2]+uc[i2,j2]-2*sc*uc[i2,j2]+sc*uc[i2-1,j2],uc[i2,j2]*(1-2*sc)+sc*(uc[i2+1,j2]+uc[i2-1,j2]))  #  sc*uc[i2+1,j2]+(1-2*sc)*uc[i2,j2]+sc*uc[i2-1,j2]竟然和sc*uc[i2+1,j2]+uc[i2,j2]-2*sc*uc[i2,j2]+sc*uc[i2-1,j2]不相等！
    #print(sc*uc[i2+1,j2]+(1-2*sc)*uc[i2,j2]+sc*uc[i2-1,j2],uhc[i2,j2]*k1r-uc[i2,j2]*uoh[i2,j2]*k1f,uhc[i2,j2],uoh[i2,j2])
    #print(uco[i2,j2],uhc[i2,j2],uoh[i2,j2])
    #print(-c_consumption/dc,oh_formation/doh,1-2*sc,1-2*shc,1-2*sco,1-2*soh)
    print(uc[:,M]) #-->uc[1,1]>uc[0,1]=c_eq说明在i=1，时间+s时，其余影响项hc，co，oh会额外产生co2，说明体系未平衡，这是有问题的，概率为平衡参数的误差有关。这导致了在第二个时间s中，扩散项由于扩散系数除以步长很大，变为了一个较大的负数
    #缩小时间步长后精度上升，尝试采用精确四舍五入

    # 2022.2.19 对所有的数值分析，都要考虑数值稳定性的问题！！唉，一叶障目，有时候是一片又厚又宽的叶子，多看看哲学吧！ 在B站国外教程上看到的冯诺依曼分析是其一种，但要使用冯诺依曼稳定性分析，需要满足lax等价定理，此处我先不考虑，直接带入冯诺伊曼分析的结论， D*δt/δx^2 (或δx) <=0.5, 对于本模型，所有的s系列参数都不满足
    ss = 1
    print(h*sc*ss,h*shc*ss,h*sco*ss,h*soh*ss, doh*s/h)  # 若要满足更稳定的条件还需在乘h后<=0.5
    '''fig = plt.figure()
    ax = fig.axes(projection='3d')
    _X_ = np.arange(0,N+1,h)
    _Y_ = np.arange(0,M+1,s)
    ax.plot_surface(_X_,_Y_,uc)'''



    fco = 'E:\\Study\\program - CO2 concentration model for CRR\\py-PDE\\simplify-co2'
    fhco3 = 'E:\\Study\\program - CO2 concentration model for CRR\\py-PDE\\simplify-hco3-'
    fco3 = 'E:\\Study\\program - CO2 concentration model for CRR\\py-PDE\\simplify-co3-'
    foh = 'E:\\Study\\program - CO2 concentration model for CRR\\py-PDE\\simplify-oh-'  
    '''    
    np.savetxt(fco,uc)
    np.savetxt(fhco3,uhc)
    np.savetxt(fco3,uco)
    np.savetxt(foh,uoh)
    '''

def PDE_2():   #   参数单位改换, 且为0.1M KHCO3
    # 时间 s 距离cm
    h = 0.0002;
    N = 50  # h*N = 100um or 0.01 cm,
    s = 0.0002;
    M = 60  # s*M= 30s

    #浓度 mmol/ml
    c_eq = 0.0342
    hc_eq = 0.099
    co_eq = 3.1*10**-5
    oh_eq = 6.6*10**-8

    #扩散系数  cm2/s
    dc = 1.91 * 10 ** -5
    dhc = 9.23 * 10 ** -6
    dco = 1.19 * 10 ** -5
    doh = 5.27 * 10 ** -5
    '''
        K1: co2+oh- == hco3-
        k2: hco3+oh == co3 + h2o
    '''
    k1f = 5930
    k1r = k1f / hc_eq * c_eq * oh_eq  # 1.3386 * 10 ** -4
    k2f = 10 ** 8
    k2r = 2.15*10**4  #k2f / co_eq * hc_eq * oh_eq  # 2.147766323 * 10 ** 4

    sc = s * dc / h ** 2
    shc = s * dhc / h ** 2
    sco = s * dco / h ** 2
    soh = s * doh / h ** 2

    c_consumption = (5 / 96485) * (0.25 / 8 + 0.1 / 2 + 0.05 / 2 + 0.4 / 12)  # j(c/cm2s)/F(c/mol)*10**-3 与 D(cm2/s)*δC/δx（mmol/cm3/cm）量纲统一，为mmol/cm2/s
    oh_formation = (5 / 96485) * (0.1 / 2 + 0.1 / 2 + 0.25 + 0.2)

    # 建立网格
    uc = np.zeros([N + 1, M + 1])
    uhc = np.zeros([N + 1, M + 1])
    uco = np.zeros([N + 1, M + 1])
    uoh = np.zeros([N + 1, M + 1])

    # 初始化
    for i in range(0, N + 1):
        uc[i, 0] = c_eq
        uhc[i, 0] = hc_eq
        uco[i, 0] = co_eq
        uoh[i, 0] = oh_eq
    for j in range(0, M + 1):
        uc[0, j] = c_eq
        uhc[0, j] = hc_eq
        uco[0, j] = co_eq
        uoh[0, j] = oh_eq
    # PDE离散化
    for j in range(0, M):
        for i in range(1, N):
            '''uc[i,j+1] = sc*uc[i+1,j]+(1-2*sc)*uc[i,j]+sc*uc[i-1,j]+s*(uhc[i,j]*k1r-uc[i,j]*uoh[i,j]*k1f)
            uhc[i,j+1] = shc*uhc[i+1,j]+(1-2*shc)*uhc[i,j]+shc*uhc[i-1,j]+s*(uc[i,j]*uoh[i,j]*k1f-uhc[i,j]*k1r-uhc[i,j]*uoh[i,j]*k2f+uco[i,j]*k2r)
            uco[i,j+1] = sco*uco[i+1,j]+(1-2*sco)*uco[i,j]+sco*uco[i-1,j]+s*(uhc[i,j]*uoh[i,j]*k2f-uco[i,j]*k2r)
            uoh[i,j+1] = soh*uoh[i+1,j]+(1-2*soh)*uoh[i,j]+soh*uoh[i-1,j]+s*(uhc[i,j]*k1r-uc[i,j]*uoh[i,j]*k1f+uco[i,j]*k2r-uhc[i,j]*uoh[i,j]*k2f)
            '''
            uc[i, j + 1] = sc * uc[i + 1, j] + (1 - 2 * sc) * uc[i, j] + sc * uc[i - 1, j] + s * ( uhc[i, j] * k1r - uc[i, j] * uoh[i, j] * k1f)
            uhc[i, j + 1] = shc * uhc[i + 1, j] + (1 - 2 * shc) * uhc[i, j] + shc * uhc[i - 1, j] + s * ( uc[i, j] * uoh[i, j] * k1f - uhc[i, j] * k1r - uhc[i, j] * uoh[i, j] * k2f + uco[i, j] * k2r)
            uco[i, j + 1] = sco * uco[i + 1, j] + (1 - 2 * sco) * uco[i, j] + sco * uco[i - 1, j] + s * ( uhc[i, j] * uoh[i, j] * k2f - uco[i, j] * k2r)
            uoh[i, j + 1] = soh * uoh[i + 1, j] + (1 - 2 * soh) * uoh[i, j] + soh * uoh[i - 1, j] + s * (uhc[i, j] * k1r - uc[i, j] * uoh[i, j] * k1f + uco[i, j] * k2r - uhc[i, j] * uoh[i, j] * k2f)
            if uoh[i,j+1]<=0:
                uoh[i,j+1]*=0
            # if uc[i,j+1]<0:
            # uc[i,j+1] = 0.000
            # continue

        # 电极边界
        uc[N, j + 1] = uc[N - 1, j + 1] - c_consumption/dc * h*s
        uhc[N, j + 1] = uhc[N - 1, j + 1]
        uco[N, j + 1] = uco[N - 1, j + 1]
        uoh[N, j + 1] = uoh[N - 1, j + 1] + oh_formation/doh * h*s
    # print(sc,sc*uc[2,1]+(1-2*sc)*uc[1,1]+sc*uc[0,1],s*(uhc[1,1]*k1r-uc[1,1]*uoh[1,1]*k1f),' --- ',uc[1,1],uhc[1,1],uoh[1,1])
    i2 = N - 1
    j2 = 5
    #print(uc[i2+1,j2],uc[i2,j2],uc[i2-1,j2],sc*uc[i2+1,j2]+uc[i2,j2]-2*sc*uc[i2,j2]+sc*uc[i2-1,j2],uc[i2,j2]*(1-2*sc)+sc*(uc[i2+1,j2]+uc[i2-1,j2]))  #  sc*uc[i2+1,j2]+(1-2*sc)*uc[i2,j2]+sc*uc[i2-1,j2]竟然和sc*uc[i2+1,j2]+uc[i2,j2]-2*sc*uc[i2,j2]+sc*uc[i2-1,j2]不相等！
    print('\033[0;35mpart of oh\033[m',soh * (uoh[i2 + 1, j2-1]+uoh[i2 - 1, j2-1]) + (1 - 2 * soh) * uoh[i2, j2-1],'\033[36mreaction part\033[m' ,s * (uhc[i2, j2-1] * k1r - uc[i2, j2-1] * uoh[i2, j2-1] * k1f),s*( uco[i2, j2-1] * k2r )-s*( uhc[i2, j2-1] * uoh[i2, j2-1] * k2f),'--u=',uco[i2, j2-1],uhc[i2, j2-1],uoh[i2, j2-1])
    #print('\033[32m reaction rate constant\033[0m',k1f,k1r,k2f,k2r,round(k2f*0.099*6.6*10**-8-k2r*3.1*10**-5,15))
    #print('\033[0;36m consumption and lamda\033[m',-c_consumption/dc*h*s,oh_formation/doh*h*s,'\n---',sc,shc,sco,soh)
    print(j2,uc[45:N+1,j2]*1000,'\n',uoh[45:N+1,j2-1],uoh[N,j2],'\n',uco[45:N+1,j2-1],'\n',uhc[45:N+1,j2-1])  #确定c——oh先出问题，可能oh——form太多导致叠加出问题---非生成问题，为K2R K2F变化太快导致时间不长不够小


    #print(k1r,k2r,'\n', sc , shc , sco,  soh  )  # 若要满足更稳定的条件还需在乘h后<=0.5

PDE_2()
