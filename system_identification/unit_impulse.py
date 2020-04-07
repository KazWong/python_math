import control
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
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
plt.plot(omega, phase)


mag, phase, omega = H.freqresp(omega)
plt.figure()
plt.grid(True)
plt.xlim(0, 4)
mag = np.reshape(mag, -1)
phase = np.reshape(phase, -1)
plt.plot(omega, mag)
plt.plot(omega, phase)


T, yout = control.impulse_response(H, range(0, 200))
plt.figure()
plt.grid(True)
plt.plot(T, yout)

#impulse response
N = 201
yout1 = [H( np.exp( complex(0, 2*math.pi*k/N) ) )  for k in range(0, N-1)]
yif = ifft(yout1)
T = np.linspace(0, 200, 200)
plt.figure()
plt.plot(T, yif)

#dft
N = 201
#yf = fft(yout)
yf = [np.sum( [yout[n]*np.exp( complex(0, -2*math.pi*k*n/N) )  for n in range(0, N-1)] ) for k in range(0, N-1)]
Y = np.abs(yf[0:100])
T = np.linspace(0, 3.1415926, 100)
plt.figure()
plt.grid(True)
plt.plot(T, Y)


plt.show()
