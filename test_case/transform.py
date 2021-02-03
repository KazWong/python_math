import numpy as np
import math
import matplotlib.pyplot as plt
from ..dynamic_systems.motion import Translation1D, Rotation1D
from ..simtools import *

sampling_rate = 1000.;end_time = 5.
clock = Time(1./sampling_rate)


### Transform
plt.figure()
plt.xlabel('x')
plt.ylabel('y')

x0 = Transform('map', 'x', 0, 0, 0)
x1 = Transform('map', 'x', 1, 0, 0)
x2 = Transform('map', 'x', -1, 0, 0)
x3 = Transform('map', 'x', 0, -1, 0)
dx = [0.0, 1.0, 0.0]
r = math.pi

plt.scatter(x1.x(), x1.y(), c='r', s=20.0)
plt.scatter(x2.x(), x2.y(), c='r', s=20.0)
plt.scatter(x3.x(), x3.y(), c='r', s=20.0)


plt.scatter(x0.x(), x0.y(), c='r', s=10.0)
x1 = x0.Translate(dx)
plt.scatter(x0.x(), x0.y(), c='b', s=10.0)
x2 = x0.RotateZ(r)
plt.scatter(x0.x(), x0.y(), c='g', s=10.0)

plt.show()
