import math
import numpy as np
import matplotlib.pyplot as plt

pi = math.pi
R = 47000
C = 47e-9

omega_c = 1/(R*C)

def H(freq):
  h = 1/complex(1,(2*pi*freq)/(omega_c))
  return h

bandwidth = np.linspace(1,10000, num=1000000)
Adb = []
phase = []
for i in bandwidth:
  Adb.append( 20*math.log(abs(H(i))) )
  phase.append(-math.atan((2*pi*i)/(omega_c)))

plt.subplot(211)
plt.xscale("log")
plt.xlabel('Frequency')
plt.ylabel('Gain')
plt.plot(bandwidth, Adb)
plt.subplot(212)
plt.xscale("log")
plt.xlabel('Frequency')
plt.ylabel('Phase')
plt.plot(bandwidth, phase)
plt.show()
