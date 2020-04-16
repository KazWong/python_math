import math
import numpy as np
#from . import Dynsys
import matplotlib.pyplot as plt

sample = 100000
t = np.linspace(0.0, 4, sample+1)
v = -t**2 + 4*t + 1

plt.figure()
plt.plot(t, v)

dt = t[1] - t[0]
s = 0.0
so = 0.5#0.1565*np.pi/150.
p = []

for i in range(0, len(t)):
  s = v[i]*dt+s
  if (s >= so):
    p = np.append(p, [dt*i])
    s = 0.0

l = np.ones(len(p))

#print(s)
plt.figure()
plt.stem(p, l, '-')


plt.show()
