import numpy as np
import math
import matplotlib.pyplot as plt
from ..sensor.speedout import SpeedOut
from ..simtools import *
from ..simtools.gaussian import LinearGaussian, SineGaussian

sampling_rate = 1000.;end_time = 60.
clock = Time(1./sampling_rate)


### SpeedOut
t = np.linspace(0, 60, 60001)
s0 = 0.*t
s1 = 1.*t
s2 = 0.8*t*t
#s3 = 1.2*t
i = 0
speed_out0 = SpeedOut(30/math.pi, 10)
speed_out1 = SpeedOut(30/math.pi, 10)
speed_out2 = SpeedOut(30/math.pi, 10)
#speed_out3 = SpeedOut(0.1565, 5)
clock.Reset()
while (clock.now() < end_time):
    clock.Tick()
    speed_out0.Update(s0[i])
    speed_out1.Update(s1[i])
    speed_out2.Update(s2[i])
    #speed_out3.Update(s3[i])
    i += 1

if ( (speed_out0.Y() != s0).any() ):
    print('Sensor-speedout: Fail in 1-1')
    raise AssertionError()

p1 = 0*speed_out1.timespace() + 1
p2 = 0*speed_out2.timespace() + 1

plt.figure()
plt.xlabel('t')
plt.ylabel('speedout')
plt.scatter(clock.timespace(), s1, c='r', s=0.5)
plt.stem(speed_out1.timespace(), p1, '-', use_line_collection=True)

plt.figure()
plt.xlabel('t')
plt.ylabel('speedout')
plt.scatter(clock.timespace(), s2, c='r', s=0.5)
plt.stem(speed_out2.timespace(), p2, '-', use_line_collection=True)
"""
plt.figure()
plt.xlabel('t')
plt.ylabel('speedout')
plt.scatter(clock.timespace(), s3, c='r', s=0.5)
plt.stem(clock.timespace(), speed_out3.Y(), '-', use_line_collection=True)
"""

plt.show()
