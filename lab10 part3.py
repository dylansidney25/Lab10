import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = plt.axes(projection="3d")
z_line = np.linspace(0, 15, 1000)
x_line = np.exp(-0.1*z_line) * np.cos(z_line)
y_line = np.exp(-0.1*z_line) * np.sin(z_line)

ax.plot3D(x_line, y_line, z_line, 'red')
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

plt.show()
