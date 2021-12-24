import matplotlib
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('bmh')

# 正常显示中文字体
plt.rcParams['font.sans-serif']=['Microsoft YaHei']

# 生成一张12*4的图
fig = plt.figure(figsize=(12,4))

# 生成第一个子图在1行2列第一列位置
ax1 = fig.add_subplot(121)

# 生成第二子图在1行2列第二列位置
ax2 = fig.add_subplot(122)

# 柱状图数据
x1 = [0.3, 1.7, 4, 6, 7]
y1 = [5, 20, 15, 25, 10]

# 折线图数据
x2 = np.arange(0,10)
y2 = [25,2,12,30,20,40,50,30,40,15]

# 第一个子图绘图和设置
ax1.bar(x1,y1)
ax1.set(xlabel='横坐标',ylabel='纵坐标',title='我在第一列位置')

# 第二个子图绘图和设置
ax2.plot(x2,y2)
ax2.set(xlabel='横坐标',ylabel='纵坐标',title='我在第二列位置')

plt.show()