import numpy as np
import math
import matplotlib.pyplot as plt
from ..simtools import *

step = 0.2;end_time = 4.0
size = 21
clock = Time(step, end_time)


# Offline time
clock.Offline(end_time)
if (clock.time.timespace[0] != 0.):
    print('Time: Fail in 1-1')
    print(clock.time.timespace[0])
    raise AssertionError()
if (clock.time.timespace[-1] < end_time):
    print('Time: Fail in 1-2')
    print(clock.Len(), clock.time.timespace[-1])
    print(end_time)
    raise AssertionError()


# Tick time and timespace consistency
tick = np.array([])
clock.Reset()
for _ in range(size):
    clock.Tick()
    tick = np.append(tick, np.around(clock.now(), 9) )
timespace = np.around(clock.time.timespace, 9)
if (tick[0] != timespace[0]) or (tick[0] != 0.0):
    print('Time: Fail in 2-1')
    print(timespace[0])
    print(tick[0])
    raise AssertionError()
if (tick[-1] != timespace[-1]) or (tick[-1] < end_time):
    print('Time: Fail in 2-2')
    print(timespace[-1])
    print(tick[-1])
    print(end_time)
    raise AssertionError()
if (tick.size != clock.Len()):
    print('Time: Fail in 2-3')
    print(tick.size, clock.Len())
    print("t=0:  ", tick[0], timespace[0])
    print("t=1:  ", tick[1], timespace[1])
    print("t=2:  ", tick[2], timespace[2])
    print("t=-2: ", tick[-2], timespace[-2])
    print("t=-1: ", tick[-1], timespace[-1])
    raise AssertionError()
if ( tick != timespace ).any():
    print('Time: Fail in 2-4')
    raise AssertionError()


# Tick after Offline
clock.Reset()
clock.Offline(end_time)
tick = clock.time.timespace
for _ in range(size, 2*size-1):
    clock.Tick()
    tick = np.append(tick, np.around(clock.now(), 3) )
timespace = np.around(clock.time.timespace, 3)
if (clock.time.timespace[0] != 0.):
    print('Time: Fail in 3-1')
    raise AssertionError()
if (clock.time.timespace[-1] != 2*end_time):
    print('Time: Fail in 3-2')
    print(clock.time.timespace[-1])
    print(tick[-1])
    print(2*end_time)
    raise AssertionError()
clock.Reset()


#Share time
clock.Offline(end_time)
clock1 = t()

class test:
    time = None
    def __init__(self):
        self.time = t()
    def now(self):
        return self.time.timespace[-1]

clock2 = test()

if (clock.now() != clock1.now() or clock.now() != clock2.now()):
    print('Time: Fail in 4-1')
    print(clock.now(), clock1.now(), clock2.now())
    raise AssertionError()


#integration
init_yy = 0.0
yy = [init_yy]
dydx = []
dt = clock.T()
x = clock.Offline(2.)
y = -x**2. + 2.*x - 0.5
for i in range(clock.Len()):
    yy = np.append(yy, [y[i] * dt + yy[-1]])
yy = np.delete(yy, 0, 0)
dydx = np.append(None, [(y[i] - y[i-1]) / dt for i in range(1, clock.Len())])

plt.figure()
plt.plot(x, y, label="y")
plt.plot(x, yy, label="In y")
plt.plot(x, dydx, label="dydx")
plt.legend()
plt.show()
