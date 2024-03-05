import numpy as np
import matplotlib.pyplot as plt

# 构造阿基米德螺旋线的参数
a = 0.8
b = 0.4
theta = np.linspace(0, 10*np.pi, 1000)
r = a + b*theta

# 极坐标系下绘制阿基米德螺旋线
fig1 = plt.figure()
ax1 = fig1.add_subplot(111, projection='polar')
ax1.plot(theta, r)

# 直角坐标系下绘制阿基米德螺旋线
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
x = r * np.cos(theta)
y = r * np.sin(theta)
ax2.plot(x, y)

# 显示图形
plt.show()