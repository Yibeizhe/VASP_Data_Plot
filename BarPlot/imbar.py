import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.set(xlim=(0,10), ylim=(0,1), autoscale_on=False)

a = np.array([[1, 1],
              [2, 2]])

N = 10
x = np.arange(N) + 0.15
y = np.random.rand(N)

width = 0.4
for x, y in zip(x, y):
    ax.imshow(a, interpolation='bicubic', extent=(x, x+width, 0, y), cmap=plt.cm.Blues_r)

ax.set_aspect('auto')
plt.show()