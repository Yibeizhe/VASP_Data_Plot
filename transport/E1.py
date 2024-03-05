import matplotlib.pyplot as plt
import numpy as np
a=5.6999479133550093
b=3.2908196842150277
# x direction mobility
strain=np.array([0.98,0.985,0.99,0.995,1,1.005,1.01,1.015,1.02])-1
print(strain)
delta_cbm=np.array([-5.0819,-5.0836,-5.0859,-5.0879,-5.0888,-5.0917,-5.0934,-5.0946,-5.0961])
print(delta_cbm)
delta_vbm=np.array([-5.8948,-5.8892,-5.8835,-5.877,-5.8684,-5.8606,-5.8512,-5.8404,-5.8291])
energy_x=np.array([-46.49365992,-46.50133984,-46.50693488,-46.51040936,-46.51170854,-46.51076528,-46.50757623,-46.50211832,-46.49435151])
E1x=np.polyfit(strain,delta_cbm,1)
e1=np.poly1d(E1x)
print("E1x:\n ",e1)
c2x=np.polyfit(strain,energy_x,2)
c2x_para=np.poly1d(c2x)
c2x_1=44.23
print("C2x: ")
print(2*c2x_1*1.6*10/(a*a))
print(c2x_para)
# plt.plot(strain,delta_cbm)
# plt.show()

#y direction mobility
delta_vbm_y=np.array([-5.8986,-5.8917,-5.884,-5.8773,-5.8684,-5.86,-5.8511,-5.8428,-5.8332])
delta_cbm_y=np.array([-5.0806,-5.083,-5.0847,-5.088,-5.0888,-5.0911,-5.0925,-5.0953,-5.0962])
energy_y=np.array([-46.49218683,-46.50074643,-46.50678016,-46.51040185,-46.51170854,-46.5107792,-46.5077217,-46.50262287,-46.49554834
])
E1y=np.polyfit(strain,delta_cbm_y,1)
e1y=np.poly1d(E1y)
print("E1y:\n ",e1y)
print(E1y,'gggg')

c2y=np.polyfit(strain,energy_y,2)
c2y_para=np.poly1d(c2y)
c2y_1=44.59

print("C2y:")
print(2*c2y_1*1.6*10/(a*a))
# plt.plot(strain,delta_cbm_y)
# plt.show()