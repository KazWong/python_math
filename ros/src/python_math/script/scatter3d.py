from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np





raw = pd.read_csv("bubble.csv", header=None, names=['cx', 'cy', 'vx', 'vy', 'wz'])
    
x = np.array(raw['cx'].tolist())
y = np.array(raw['cy'].tolist())
z = np.array(raw['vx'].tolist())

x = (x - 80) * 0.05
y = (y - 80) * 0.05

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y, z, c=(0.1, 0.2, 0.5, 0.3), marker='o')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('VX')

x = np.array(raw['cx'].tolist())
y = np.array(raw['cy'].tolist())
z = np.array(raw['vy'].tolist())

x = (x - 80) * 0.05
y = (y - 80) * 0.05

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y, z, c=(0.1, 0.2, 0.5, 0.3), marker='o')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('VY')

x = np.array(raw['cx'].tolist())
y = np.array(raw['cy'].tolist())
z = np.array(raw['wz'].tolist())

x = (x - 80) * 0.05
y = (y - 80) * 0.05

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y, z, c=(0.1, 0.2, 0.5, 0.3), marker='o')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('WZ')

plt.show()
