import numpy as np
import math
import matplotlib.pyplot as plt
from ..dynamic_systems.motion import Translation1D, Rotation1D
from ..simtools import *
from ..simtools.plotlib import *

sampling_rate = 1000.;end_time = 5.
clock = Time(1./sampling_rate)


### Transform
plt.figure()
plt.xlabel('x')
plt.ylabel('y')
plt.gca().set_aspect('equal')        # Set aspect ratio
plt.xlim(-2, 2)                    # Set x-axis range
plt.ylim(-2, 2)                    # Set y-axis range

x0 = Frame([0., 0., 0.], [0., 0., 0.])
xx0 = Frame([0., 0., 0.], [0., 0., 0.])
x1 = Frame([1., 0., 0.], [0., 0., 0.])
x2 = Frame([-1., 0., 0.], [0., 0., 0.])
x3 = Frame([0., -1., 0.], [0., 0., 0.])
dx = [0.0, 0.5, 0.0]
dxx = [0.2, 0.5, 0.0]
r0 = [0.0, 0.0, 0.0]
r = [0.0, 0.0, -math.pi/4]

#Frame(x1.pos(), x1.rpy())
#Frame(x2.pos(), x2.rpy())
#Frame(x3.pos(), x3.rpy())

PlotFrame(x0)
plt.scatter(x0.x(), x0.y(), c='r', s=10.0)

x0.Translate(dx)
PlotPose(x0.pos(), x0.rpy())
plt.scatter(x0.x(), x0.y(), c='b', s=10.0)

x0.RotateYaw(r[2])
PlotFrame(x0)
plt.scatter(x0.x(), x0.y(), c='g', s=10.0)

x0.Translate(dx)
PlotPose(x0.pos(), x0.rpy())
plt.scatter(x0.x(), x0.y(), c='g', s=10.0)

xx0.Transformation(dxx, r)
PlotFrame(xx0)
plt.scatter(xx0.x(), xx0.y(), c='m', s=10.0)

xx0.Transformation(dxx, r)
PlotPose(xx0.pos(), xx0.rpy())
plt.scatter(xx0.x(), xx0.y(), c='m', s=10.0)

plt.show()
