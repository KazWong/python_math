import control
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import numpy as np
import math

z = control.TransferFunction.z
H = (0.9474+0.2105*z**-1-0.7368*z**-2)/(1.0-1.579*z**-1+0.7895*z**-2)

omega = np.linspace(0, 3.1415926, 500)
mag, phase, omega = control.bode(H, omega=omega, Plot=False)
plt.figure()
plt.grid(True)
#plt.xscale('log')
#plt.xticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3])
#plt.xticks([0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#plt.yscale('log')
#plt.yticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
plt.xlim(0, 4)
plt.plot(omega, mag)


Nt = 50
N = 201
A = 1.
l = 7.

n = range(0, Nt + N - 1)

#for l in range(1, int((N - 1)/2) ):
ohml = 2.*math.pi*l / N
u = A*np.cos([ohml*x for x in n])
ye = H(ohml)
#ue = np.append( ue, u )
#ye = np.append( ye, H(ohml)*u )
	
n = range(0, u.size)
Y = ye
plt.figure()
plt.grid(True)
#plt.xscale('log')
#plt.xticks([0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 2, 3])
#plt.yscale('log')
#plt.yticks([0.001, 0.1, 10])
plt.xlim(0, 250)
plt.ylim(-6, 6)
line_up, = plt.plot(n, u, label="u")
line_down, = plt.plot(n, Y, label="y")
plt.legend(handles=[line_up, line_down])

print(H(ohml))


#plt.figure()
#Yf = fft(ye)
#Uf = fft(ue)

#half = int(ye.size/2)
#Y = Yf[0:half]
#U = Uf[0:half]

#H = np.abs(Y/U)
#X = np.linspace(0, 3.1415926, ye.size)
#plt.grid(True)
#plt.xscale('log')
#plt.xticks([0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 2, 3])
#plt.yscale('log')
#plt.yticks([0.001, 0.1, 10])
#plt.xlim(0.01, 4)
#plt.ylim(0.0001, 10)
#plt.plot(X, ye)

plt.show()
