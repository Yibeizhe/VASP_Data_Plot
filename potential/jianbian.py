import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# 创建数据
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 创建渐变颜色填充
gradient = np.linspace(0, 1, len(x))
colors = plt.cm.viridis(gradient)

# 绘制线图
fig, ax = plt.subplots()
ax.plot(x, y, linewidth=2)

# 填充渐变颜色
poly = Polygon(np.column_stack([x, y]), facecolor='none', edgecolor='none')
ax.add_patch(poly)
ax.autoscale_view()

ax.fill_between(x, y, where=y >= 0, interpolate=True, color=colors, alpha=0.7)
ax.fill_between(x, y, where=y <= 0, interpolate=True, color=colors, alpha=0.7)

plt.show()