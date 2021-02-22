import numpy as np
import math
import sys
import matplotlib.pyplot as plt
from ..simtools import *

print('********************************************************************')
print('')
print('Time:')

TEST_COUNT = 0

#init
print('\tTest init\t\t', end =" ");TEST_COUNT += 1
sampling_freq = 1000.0;end_time = 4.0
t = t()
clock = Time(1./sampling_freq)
clock1 = Time(1.0)

list1 = np.array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.])
list2 = np.array([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10., 15., 20., 25., 30.])

clock1.Offline(10.0)
if ( clock.count() != 10 or clock1.count() != 10 ):
    print('Time: Fail in ', TEST_COUNT, '-1')
    print(list1)
    print(clock.count())
    print(clock1.count())
    raise AssertionError()
if ( clock.Len() != 11 or clock1.Len() != 11 ):
    print('Time: Fail in ', TEST_COUNT, '-2')
    print(list1)
    print(clock.time.timespace())
    print(clock1.time.timespace())
    raise AssertionError()
if ( (clock.timespace() != list1).any() or (clock1.timespace() != list1).any() ):
    print('Time: Fail in ', TEST_COUNT, '-3')
    print(list1)
    print(clock.time.timespace())
    print(clock1.time.timespace())
    raise AssertionError()
if ( clock.step() != 1.0 or clock1.step() != 1.0 ):
    print('Time: Fail in ', TEST_COUNT, '-4')
    print(clock.step())
    print(clock1.step())
    raise AssertionError()
if ( clock.now() != 10. or clock1.now() != 10. ):
    print('Time: Fail in ', TEST_COUNT, '-5')
    print(list1)
    print(clock.count())
    print(clock1.count())
    raise AssertionError()

clock2 = Time(5.0)
clock2.Offline(29.0)
if ( clock.count() != 14 or clock1.count() != 14 or clock2.count() != 14 ):
    print('Time: Fail in ', TEST_COUNT, '-1')
    print(list2)
    print(clock.time.timespace())
    print(clock1.time.timespace())
    print(clock2.time.timespace())
    raise AssertionError()
if ( clock.Len() != 15 or clock1.Len() != 15 or clock2.Len() != 15 ):
    print('Time: Fail in ', TEST_COUNT, '-2')
    print(list2)
    print(clock.time.timespace())
    print(clock1.time.timespace())
    print(clock2.time.timespace())
    raise AssertionError()
if ( (clock.timespace() != list2).any() or (clock1.timespace() != list2).any() or (clock2.timespace() != list2).any() ):
    print('Time: Fail in ', TEST_COUNT, '-3')
    print(list2)
    print(clock.time.timespace())
    print(clock1.time.timespace())
    print(clock2.time.timespace())
    raise AssertionError()
print('Pass')

# Offline
print('\tTest Offline\t\t', end =" ");TEST_COUNT += 1
clock.Offline(end_time)
if (clock.time.timespace()[0] != 0.):
    print('Time: Fail in ', TEST_COUNT, '-1')
    print(clock.time.timespace[0])
    raise AssertionError()
if (clock.time.timespace()[-1] < end_time):
    print('Time: Fail in ', TEST_COUNT, '-2')
    print(clock.Len(), clock.time.timespace[-1])
    print(end_time)
    raise AssertionError()
print('Pass')

# Tick time and timespace consistency
print('\tTest Tick\t\t', end =" ");TEST_COUNT += 1
tick = np.array([]);size = 21
clock.Reset()
for _ in range(size):
    clock.Tick()
    tick = np.append(tick, np.around(clock.now(), 9) )
timespace = np.around(clock.time.timespace(), 9)
if (tick[0] != timespace[0]) or (tick[0] != 0.0):
    print('Time: Fail in ', TEST_COUNT, '-1')
    print(timespace[0])
    print(tick[0])
    raise AssertionError()
if (tick[-1] != timespace[-1]) or (tick[-1] < end_time):
    print('Time: Fail in ', TEST_COUNT, '-2')
    print(timespace[-1])
    print(tick[-1])
    print(end_time)
    raise AssertionError()
if (tick.size != clock.Len()):
    print('Time: Fail in ', TEST_COUNT, '-3')
    print(tick.size, clock.Len())
    print("t=0:  ", tick[0], timespace[0])
    print("t=1:  ", tick[1], timespace[1])
    print("t=2:  ", tick[2], timespace[2])
    print("t=-2: ", tick[-2], timespace[-2])
    print("t=-1: ", tick[-1], timespace[-1])
    raise AssertionError()
if ( tick != timespace ).any():
    print('Time: Fail in ', TEST_COUNT, '-4')
    raise AssertionError()
print('Pass')

# Tick after Offline
print('\tTest Tick+Offline\t', end =" ");TEST_COUNT += 1
sampling_freq = 1000.0;end_time = 4.0
clock = Time(1./sampling_freq)
clock.Reset()
clock.Offline(end_time)
tick = clock.time.timespace()
while (tick[-1] < 2*end_time):
    clock.Tick()
    tick = np.append(tick, np.around(clock.now(), 3) )
timespace = np.around(clock.time.timespace(), 3)
if (clock.time.timespace()[0] != 0.):
    print('Time: Fail in ', TEST_COUNT, '-1')
    raise AssertionError()
if (clock.time.timespace()[-1] != 2*end_time):
    print('Time: Fail in ', TEST_COUNT, '-2')
    print(clock.time.timespace()[-1])
    print(tick[-1])
    print(2*end_time)
    raise AssertionError()
clock.Reset()
print('Pass')

#Share time
print('\tTest Share time\t\t', end =" ");TEST_COUNT += 1
clock.Offline(end_time)
time1 = t

class test:
    time = None
    def __init__(self):
        self.time = t
    def now(self):
        return self.time.timespace()[-1]

clock2 = test()

if (clock.now() != time1.now() or clock.now() != clock2.now()):
    print('Time: Fail in ', TEST_COUNT, '-1')
    print(clock.now(), time1.now(), clock2.now())
    raise AssertionError()
print('Pass')

print()


#integration
clock.Reset()

init_yy = 0.0
yy = [init_yy]
dydx = []
dt = time1.step()
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

if (len(sys.argv) > 1):
    if (bool(sys.argv[1]) is True):
        plt.show()
