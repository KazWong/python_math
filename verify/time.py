import numpy as np
import math
import matplotlib.pyplot as plt
from ..signal import Signal, Ideal, Time

sampling_rate = 1000.;end_time = 4.
clock = Time(sampling_rate)

# Offline time
clock.Offline(end_time)
if (clock.Hz() != sampling_rate): raise AssertionError()
if (clock.T() != 1./sampling_rate): raise AssertionError()
if (clock.timespace[0] != 0.): raise AssertionError()
if (clock.timespace[-1] != end_time):
  print(clock.timespace[-1]) 
  print(end_time[-1]) 
  raise AssertionError()
clock.Reset()

# Tick time and timespace consistency
tick = np.array([])
for i in range(int(sampling_rate*end_time)+1):
  tick = np.append(tick, np.around(clock.Tick(), 3) )
timespace = np.around(clock.timespace, 3)
if (tick[0] != timespace[0]) or (tick[0] != 0.0): 
  print(timespace[0])
  print(tick[0])
  raise AssertionError()
if (tick[-1] != timespace[-1]) or (tick[-1] != end_time):
  print(timespace[-1])
  print(tick[-1])
  print(end_time)
  raise AssertionError()
if (tick.size != timespace.size):
  raise AssertionError()
if ( tick != timespace ).any(): 
  raise AssertionError()
clock.Reset()

# Tick after Offline
clock.Offline(end_time)
tick = clock.timespace
for i in range(int(sampling_rate*end_time)+1, int(sampling_rate*2*end_time)+1):
  tick = np.append(tick, np.around(clock.Tick(), 3) )
timespace = np.around(clock.timespace, 3)
if (clock.timespace[0] != 0.): raise AssertionError()
if (clock.timespace[-1] != 2*end_time): 
  print(clock.timespace[-1])
  print(2*end_time)
  raise AssertionError()
clock.Reset()


#integration
yy = [0.0]
dydx = [0.0]
dt = clock.T()
x = clock.Offline(2.)
y = -x**2. + 2.*x - 0.5
for i in range(clock.Len()):
  yy = np.append(yy, [y[i] * dt + yy[-1]])
yy = np.delete(yy, 0, 0)
dydx = np.append(dydx, [(y[i] - y[i-1]) / dt for i in range(1, clock.Len())])

plt.figure()
plt.plot(x, y)
plt.plot(x, yy)
plt.plot(x, dydx)
plt.show()
