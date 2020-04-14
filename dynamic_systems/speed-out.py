import math
import numpy as np
#from . import Dynsys
import matplotlib.pyplot as plt

sample = 10000
t = np.linspace(0, 2, 10000)
v = 4*t#-t**2 + 4*t + 1

plt.figure()
plt.plot(t, v)


so = np.pi*0.1565/150.
dt = 1./sample
p = [0.0]
s = 0.0

for i in range(1, sample):
	s = np.abs(v[i] - v[i-1])*dt + s
	print(s)
	#if (s >= so):
	#	p = np.append(p, [dt*i])
	#	s = 0.0

l = np.ones(len(p))


plt.figure()
plt.stem(p, l, '-')


#plt.show()
