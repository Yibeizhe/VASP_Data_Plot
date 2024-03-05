import numpy as np
def rotaTheta(theta,vec):
    theta=theta*np.pi/180
    rotate_array = np.array([[np.cos(theta), -np.sin(theta)],
                             [np.sin(theta), np.cos(theta)]], dtype='float')
    return np.dot(rotate_array,vec)
# print(rotaTheta(60,np.array([2*3**0.5,1])))
print((10.550129-10.213)/10.550129)