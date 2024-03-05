import numpy  as np
x=-25*np.ones(5)
print(x.size)
print(x)
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# 创建一个图形对象
fig, ax = plt.subplots()

# 绘制曲线
ax.plot(x, y1, label='sin(x)')
ax.plot(x, y2, label='cos(x)')

# 填充负数区域
ax.fill_between(x, y1, y2, where=(y1 > y2), interpolate=True, color='gray', alpha=0.5)

# 添加图例
ax.legend()

# 显示图形
plt.show()






